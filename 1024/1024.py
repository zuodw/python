#coding = utf-8
import keyword
from functools import reduce

for kw in keyword.kwlist:
	print(kw)


def f(x):
	return x * x

lst = [1,2,3,4,5,6,7] 

new_list = list(map(f, lst))
new_list = list(map(str, lst))

print(new_list)


def add(x,y):
	return x + y
num = reduce(add, [1,2,3,4,5,6,7,8,9,10])
print(num)

def g(m_str):
	return m_str.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(g, L1))
print(L2)

def is_odd(x):
	return x % 2 == 1
print(list(filter(is_odd, [1,2,3,4,5,6,7])))

m_list = []
n = 3
while n < 100:
	if n % 2 == 1:
		m_list.append(n)
	n = n + 1
print(m_list)
def primes(x, n):
	return x % n != 0
filter(primes, m_list)



