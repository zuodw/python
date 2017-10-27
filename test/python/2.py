#coding:utf-8
from collections import Iterable

'''
names = ['zuodw', 'fanhx', 'zzz', 'fff', 'ddd', 'www']

print(names[3::2])

numbers = []

for i in range(100):
    numbers.append(i)

print(numbers[:-1:3])


dict = {"name":'zudow', "age":29, "job":"enginner"}

for key in dict:
    print(key)

for value in dict.values():
    print(value)

for value, key in dict.items():
    print(value, key)

print(isinstance('abcde', Iterable))
print(isinstance(12345, Iterable))
print(isinstance('abcde', Iterable))

list = ['a','b','c','d','e','f']
for i, item in enumerate(list):
    print(i, item)


list1 = [x*x for x in range(1,11) if x % 2 == 0]
print(list1)

list2 = [m + n for m in "ABC" for n in "XYZ"]
print(list2)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

lista = ()
listb = ()
dict1 = {lista:1, listb:2}


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)

def odd():
    print("step 1")
    yield 1
    print("step 2")
    yield 2
    print("step 3")
    yield 3
for i in odd():
    print(i)
'''



'''
def triangles():
    list = [1]
    while True:
        new_list = [1]
        for i in range(0, len(list)-1):
            new_list.append(list[i] + list[i + 1])
        new_list.append(1)
        list = new_list[:]
        yield new_list

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

'''



a = abs(-19)
print(a)
f = abs
print(f(-21))