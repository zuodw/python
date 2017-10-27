#coding:utf-8
from collections    import Iterable
from collections    import Iterator
from functools      import reduce
import functools

m_list = [m + n for m in 'ABC' for n in 'XYZ']
print(m_list)

d = {'A':1, 'B':2, 'C':3}
print([key + '=' + str(value) for key,value in d.items()])

for key,value in d.items():
    print(key, value)
l = ['aBc', 'msEEE', 'ASDF', 2322]
print([s.lower() for s in l if isinstance(s, str)])

print(isinstance((), tuple))

def fib(max):
    x, y, n = 1, 1, 1
    while n <= max:
        yield x
        x, y, n = y, x + y, n + 1

    return 'done'
m_g = (str(x) + '.' for x in fib(10))
for x in m_g:
    print(x)

m_num = 5
m_str = 'zippo'
m_list = ['a','b','c','d']
m_tuple = (1,2,3,4)
m_dict = {"name":"zuodw", "age":29}

print("int:",       isinstance(m_num, Iterable),    isinstance(m_num, Iterator))
print("str:",       isinstance(m_str, Iterable),    isinstance(m_str, Iterator))
print("list:",      isinstance(m_list, Iterable),   isinstance(m_list, Iterator))
print("tuple:",     isinstance(m_tuple, Iterable),  isinstance(m_tuple, Iterator))
print("dict:",      isinstance(m_dict, Iterable),   isinstance(m_dict, Iterator))
print("generator:", isinstance(m_g, Iterable),      isinstance(m_g, Iterator))

def m_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def func(x, f):
    print(f(x))

func(-5, m_abs)

print(list(map(m_abs, [-5,666,-85])))

def m_add(x, y):
    return x + y
print(reduce(m_add, [-5,666,-85]))



def str2num(str):
    def func(x, y):
        return x * 10 + y

    def ch2int(ch):
        return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[ch]

    return reduce(func, list(map(ch2int, str)))

print(str2num("123456789"))

#filter

def judge(x):
    return x % 2 == 1

print(list(filter(judge, [1,2,3,4,5,6,7,8,9])))

def judge(x):
    if x == 2:
        return True
    for n in range(2,x):
        if x % n == 0:
            return False
    return True
print(list(filter(judge, range(2,100))))


def is_palindrome(n):
    m_list = list(str(n))
    m_list_bak = m_list[:]
    m_list.reverse()
    for i in range(0, len(m_list)):
        if m_list[i] != m_list_bak[i]:
            return False
    return True

output = filter(is_palindrome, range(1, 1000))
print(list(output))

print(sorted([36, 5, -12, 9, -21]))

def func(x):
    return x * x
print(sorted([36, 5, -12, 9, -21], key = func))

print(sorted([36, 5, -12, 9, -21], key = abs, reverse = True))

print(sorted(['a', 'f','E', 'B', 'd', 'C']))

print(sorted(['a', 'f','E', 'B', 'd', 'C'], key = str.lower))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]
    
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)

def lazy_sum(*args):
    def sum():
        ret = 0
        for n in args:
            ret = ret + n
        return ret
    return sum

f = lazy_sum(1,2,3,4,5,6,7,8,9)
print(f)
print(f())

def count():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1, f2, f3= count()
print(f1(), f2(), f3())

#匿名函数
f = lambda x : x * x
print(f(5))


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print("2017-10-25")
# now = log(now)
now()

@log
def add(x, y ,*args):
    sum = x + y
    for n in args:
        sum = sum + n
    return sum
print(add(1,2,3,4,5,6,7,8,9))
print(now.__name__)

def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for t in text:
                print("%s %s" %(t, func.__name__))
            func(*args, **kw)
            print("%s %s" %('end', func.__name__))
            return
        return wrapper
    return decorator

@log('call')
def now():
    print("2017-10-25")
now()

#偏函数
def add(x, y, z):
    print(x + y + z)

add2 = functools.partial(add, y = 1, z = 2)

add(5, 9, 11)
add2(5)