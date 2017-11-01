#!/usr/bin/python
#encoding:utf-8
import  functools
from    collections     import Iterator
from    functools       import reduce

#切片
num_list = [1,2,3,4,5,6,7,8,9,10]
print(num_list[:8:2])
m_str = 'ABCDEFGHIJKLMN'
print(m_str[:8:3])

#迭代
for num in num_list:
    print(num)

dict = {'zuodw':29, 'fanhx':30}
for name in dict.keys():
    print(name)
for age in dict.values():
    print(age)
for name, age in dict.items():
    print(name, age)

#列表生成式
L1 = [x * x for x in range(0, 10)]
print(L1)

L2 = [m + n for m in "ABC" for n in "XYZ"]
print(L2)

#生成器 generator
L = (x * x for x in range(0, 4))
print(L)
#print(next(list))
for x in L:
    print('a', x)

def fib(max):
    x,y,n = 1,1,1
    while n < max:
        yield y
        x,y = y, x+y
        n = n + 1
    return 'done'

g = fib(6)
print(g)

for x in g:
    print(x)

#迭代器
#########################################################

#函数式编程

#高阶函数
def m_abs(x):
    if x >= 0:
        return x
    else:
        return -x

m_list = list(map(m_abs, [-6,23,-9,0]))
print(m_list)

def m_sum(x, y):
    return x + y

print(reduce(m_sum, [1,2,3,4,5,6,7,8,9,10]))

str_list = ['amy', 'Fanhx', 'zUODW']
print(sorted(str_list, key = str.upper, reverse = True))

#返回函数

def lazy_sum(*args):
    def m_sum():
        sum = 0
        for x in args:
            sum = sum + x
        return sum
    return m_sum

f = lazy_sum(1,2,3,4,5,6)
print(f())

#匿名函数 lambda
print(reduce(lambda x,y:x+y , [1,2,3,4,5,6,7,8,9]))

f1 = lambda x : x * x
print(f1(15))

#n装饰器
print('\n装饰器 decorator\n')

def log(*text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print(text)
            for s in text:
                print(s)
            func(*args, **kw)
            return 
        return wrapper
    return decorator


@log('call')
def now():
    print('2017-10-26')

now()

def n_add(x,y):
    print(x + y)

f_add = functools.partial(n_add, y = 2)
n_add(4,5)
f_add(4)
