import logging
logging.basicConfig(level=logging.INFO)

import aiomysql, asyncio

def log(sql, args=()):
    logging.info('SQL: %s' % sql)


async def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = await aiomysql.create_pool(
        host=kw.get('host', '127.0.0.1'),
        port=kw.get('port', 3306),
        user=kw.get('user', 'root'),
        password=kw.get('password', 'Zdw*890412'),
        db=kw.get('db', 'mysql'),
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
        )

async def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with await __pool as conn:
        cur = await conn.cursor(aiomysql.DictCursor)
        '''
        SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。
        注意要始终坚持使用带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。
        '''
        await cur.execute(sql.replace('?', '%s'), args or ())
        if size:
            rs = await cur.fetchmany(size)
        else:
            rs = await cur.fetchall()
        await cur.close()
        logging.info('rows returned: %s.' % len(rs))
        return rs

'''
要执行INSERT、UPDATE、DELETE语句，可以定义一个通用的execute()函数，
因为这3种SQL的执行都需要相同的参数，以及返回一个整数表示影响的行数.
'''
async def execute(sql, args):
    log(sql, args)
    global __pool
    with await __pool as conn:
        try:
            cur = await conn.cursor(aiomysql.DictCursor)
            await cur.execute(sql.replace('?', '%s'), args or ())
            affected = cur.rowcount
            await cur.close()
        except BaseException as e:
            raise
        return affected

#构造sql语句参数字符串，最后返回的字符串会以','分割多个'?'，如 num==2，则会返回 '?, ?'
def create_args_string(num):
    L = []
    for n in range(num):
        L.append('?')
    return ', '.join(L)



class Field(object):
    def __init__(self, column_name, column_type, is_primary_key, default):
        self.column_name = column_name
        self.column_type = column_type
        self.is_primary_key = is_primary_key    # 是否是主键，bool类型
        self.default = default
    '''
    打印出类的类型，子类都会调用父类的__str__方法
    '''
    def __str__(self):
        return '<%s : %s>' % (self.__class__.__name__, self.column_name)

class StringField(Field):
    def __init__(self, column_name=None, column_type='varchar(100)', is_primary_key=False, default=None):
        super().__init__(column_name, column_type, is_primary_key, default)

class IntegerField(Field):
    def __init__(self, column_name=None, column_type='bigint', is_primary_key=False, default=None):
        super().__init__(column_name, column_type, is_primary_key, default)

class FloatField(Field):
    def __init__(self, column_name=None, column_type='real', is_primary_key=False, default=0.0):
        super().__init__(column_name, column_type, is_primary_key, default)

class TextField(Field):
    def __init__(self, column_name=None, column_type='text', is_primary_key=False, default=0.0):
        super().__init__(column_name, column_type, is_primary_key, default)

class BooleanField(Field):
    def __init__(self, column_name=None, column_type='boolean', is_primary_key=False, default=0.0):
        super().__init__(column_name, column_type, is_primary_key, default)



class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)

        '''
        object.get('key',default)是dict的一个方法， 可以指定key来取得value，
        并且可以指定key不存在时返回默认值.
        如果使用object['key'],key不存在时会出错。
        '''
        tableName = attrs.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))

        mappings = dict()
        fields = []
        primaryKey = None

        for k, v in attrs.items():
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

                if v.is_primary_key:
                    # 找到主键
                    if primaryKey:
                        raise RuntimeError('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                else:
                    fields.append(k)

        if not primaryKey:
            raise RuntimeError('Primary key not found.')

        for k in mappings.keys():
            attrs.pop(k)

        escaped_fields = list(map(lambda f: '`%s`' % f, fields))    # 把fields的值全部加了个 ``

        attrs['__mappings__'] = mappings; # 保存属性和列的映射关系
        attrs['__table__'] = tableName;
        attrs['__primary_key__'] = primaryKey # 主键属性名
        attrs['__fields__'] = fields # 除主键外的属性名
        # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).column_name or f), fields)), primaryKey)
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super().__init__(**kw)

    '''
    1.继承自dict => 可以使用Model[attr]的调用方式
    2.  实现__getattr__() => 可以使用Model.attr的调用方式,
        但是只能使用，不能执行赋值操作，要赋值的话还需要实现 __setattr__()
    '''
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        '''
        getattr(object, name[,default]),从object中取出name属性，可以指定default值
        '''
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                setattr(self, key, value)
        return value

    '''
    SELECT不用传入实例，只是查询数据库，所以用·类方法·。
    INSERT、UPDATE、DELETE等语句需要传入实例，因此需要添加·实例方法·。
    '''
    @classmethod
    async def find(cls, primary_key):
        # find object by primary key
        sql = '%s where `%s`=?' % (cls.__select__, cls.__primary_key__)
        rs = await select(sql, [primary_key], 1)
        if len(rs) == 0:
            return None
        return cls(**rs[0]) # 返回的是一个实例对象引用

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows :%s' % rows)

    async def update(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)
        
    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)
