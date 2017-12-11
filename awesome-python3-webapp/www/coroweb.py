import functools

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

def get_required_kw_args(fn):  # 获取无默认值的命名关键词参数
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        # 如果视图函数存在命名关键字参数，且默认值为空，获取它的key（参数名）  
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
        return tuple(args)

def get_named_kw_args(fn):  # 获取命名关键词参数
    args = []
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)

def has_named_kw_arg(fn):  # 判断是否有命名关键词参数
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True

def has_var_kw_arg(fn):  # 判断是否有关键词参数 
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True

def has_request_arg(fn):   # 判断是否含有名叫'request'的参数，且位置在最后  
    params = inspect.signature(fn).parameters  
    found = False  
    for name, param in params.items():  
        if name == 'request':  
            found = True  
            continue  
        if found and (
            param.kind != inspect.Parameter.VAR_POSITIONAL and
            param.kind != inspect.Parameter.KEYWORD_ONLY and
            param.kind != inspect.Parameter.VAR_KEYWORD):
            # 若判断为True，表明param只能是位置参数。且该参数位于request之后，故不满足条件，报错。
            raise ValueError('request parameter must be the last named parameter in function:%s%s' % (fn.__name__, str(sig)))
    return found