import functools
import inspect

# 建立视图函数装饰器，用来存储、附带URL信息 
def handler_decorator(path, *, method):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__route__ = path
        wrapper.__method__ = method
        return wrapper
    return decorator
# 偏函数。GET POST 方法的路由装饰器
get = functools.partial(handler_decorator, method='GET')
post = functools.partial(handler_decorator, method='POST')

# 使用inspect模块，检查视图函数的参数
  
# inspect.Parameter.kind 类型：
# POSITIONAL_ONLY          位置参数
# KEYWORD_ONLY             命名关键词参数
# VAR_POSITIONAL           可选参数 *args
# VAR_KEYWORD              关键词参数 **kw
# POSITIONAL_OR_KEYWORD    位置或必选参数

def get_required_kw_args(fn): # 获取无默认值的命名关键词参数
    args = []

    for name, param in inspect.signature(fn).paramters.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)

def get_named_kw_args(fn):  # 获取命名关键词参数
    args = []

    for name, param in inspect.signature(fn).parameters.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)

def has_named_kw_arg(fn):  # 判断是否有命名关键词参数
    for name, param in inspect.signature(fn).parameters.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

def has_var_kw_arg(fn):  # 判断是否有关键词参数
    for name, param in inspect.signature(fn).parameters.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True    

def has_request_arg(fn):   # 判断是否含有名叫'request'的参数，且位置在最后
    found = False
    for name, param in inspect.signature(fn).parameters.items():
        if name == 'request':
            found = True
            continue
        if found and (  
            param.kind != inspect.Parameter.VAR_POSITIONAL and   
            param.kind != inspect.Parameter.KEYWORD_ONLY and   
            param.kind != inspect.Parameter.VAR_KEYWORD):  
            raise ValueError('request parameter must be the last named parameter in function:%s%s' % (fn.__name__, str(sig)))
    return found

# 定义RequestHandler从视图函数中分析其需要接受的参数，从web.Request中获取必要的参数  
# 调用视图函数，然后把结果转换为web.Response对象，符合aiohttp框架要求
class RequestHandler(object):
    def __init__(self, app, fn):
        self._app = app
        self._func = fn
        self._required_kw_args = get_required_kw_args(fn)
        self._named_kw_args = get_named_kw_args(fn)
        self._has_request_arg = has_request_arg(fn)
        self._has_named_kw_arg = has_named_kw_arg(fn)
        self._has_var_kw_arg = has_var_kw_arg(fn)

    # 1.定义kw，用于保存参数
    # 2.判断视图函数是否存在关键词参数，如果存在根据POST或者GET方法将request请求内容保存到kw
    # 3.如果kw为空（说明request无请求内容），则将match_info列表里的资源映射给kw；若不为空，把命名关键词参数内容给kw
    # 4.完善_has_request_arg和_required_kw_args属性
    async def __call__(self, request):
        kw = None # 定义kw，用于保存request中参数

        if self._has_named_kw_arg or self.has_var_kw_arg: # 若视图函数有命名关键词或关键词参数  
            if request.method == 'POST':
                # 根据request参数中的content_type使用不同解析方法：
                if request.content_type == None: # 如果content_type不存在，返回400错误
                    return web.HTTPBadRequest(text='Missing Content_Type.')
                ct = request.content_type.lower() # 小写，便于检查
                if ct.startswith('application/json'):  # json格式数据
                    params = await request.json() # 仅解析body字段的json数据
                    if not isinstance(params, dict): # request.json()返回dict对象
                        return web.HTTPBadRequest(text='JSON body must be dict_object.')
                    kw = params
                # form表单请求的编码形式
            elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                params = await request.post() # 返回post的内容中解析后的数据。dict-like对象
                kw = dict(**params)
            else:
                return web.HTTPBadRequest(text='Unsupported Content_Type: %s' % request.content_type)
            
            if request.method = 'GET':
                qs = request.query_string # 返回URL查询语句，?后的键值。string形式。
                if qs:
                    kw = dict()
                    for k, v in parse.parse_qs(qs, True).items(): # 返回查询变量和值的映射，dict对象。True表示不忽略空格。
                        kw[k] = v[0]

        if kw is None:  # 若request中无参数
            # request.match_info返回dict对象。可变路由中的可变字段{variable}为参数名，传入request请求的path为值  
            # 若存在可变路由：/a/{name}/c，可匹配path为：/a/jack/c的request  
            # 则reqwuest.match_info返回{name = jack}
            kw = dict(**request.match_info)
        else: # request有参数
            if self._has_named_kw_arg and (not self._has_var_kw_arg): # 若视图函数只有命名关键词参数没有关键词参数                 
                copy = dict()  
                # 只保留命名关键词参数  
                for name in self._named_kw_arg:  
                    if name in kw:  
                        copy[name] = kw[name]  
                kw = copy # kw中只存在命名关键词参数  
            # 将request.match_info中的参数传入kw  
            for k, v in request.match_info.items():  
                # 检查kw中的参数是否和match_info中的重复  
                if k in kw:  
                    logging.warn('Duplicate arg name in named arg and kw args: %s' % k)   
                kw[k] = v  
        if self._has_request_arg: # 视图函数存在request参数  
            kw['request'] = request  
        if self._required_kw_args: # 视图函数存在无默认值的命名关键词参数  
            for name in self._required_kw_args:  
                if not name in kw: # 若未传入必须参数值，报错。  
                    return web.HTTPBadRequest('Missing argument: %s' % name)  
        # 至此，kw为视图函数fn真正能调用的参数  
        # request请求中的参数，终于传递给了视图函数  
        logging.info('call with args: %s' % str(kw))  
        #try:  
        r = await self._func(**kw)  
        return r  
        #except APIerror as e:  
            #return dict(error=e.error, data=e.data, message=e.message)  