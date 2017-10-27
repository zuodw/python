#coding: utf-8
str = "carplay is enable"
print(str.title())
print(str.upper())
print(str.lower())

def my_sum(a,b,*args):
	return a + b + sum(args)
print(my_sum(1,3,5))

def func(name, age, city = "beijing"):
	print('name:', name, 'age:', age, 'city:', city)

func('zuodw', 29)

def nop():
	pass
	
age = 18
if age > 18:
	print("big")
elif age == 18:
	pass
	print("equal")
else:
	print("small")

	
def points(x, y):
	x = x + 10
	y = y + 10
	return x, y
	
print(points(5,8))

def power(x, y=2):
	print(x**y)
	
power(5)
power(5,3)

def func_1(*args):
	sum = 0
	for arg in args:
		sum = sum + arg
	print("sum:", sum)
func_1(1,2,3,4,5,6,7,8,9)

def func2(name):
	print("为", name, "打call")

func2("徐英哥")


def kw_func(name, age, **kw):
	print("name:", name, "age:", age, "other:", kw)
kw_func('zuodw', 29, city = 'dalian')


def kw_func2(name, age, *, city):
	print("name:", name, "age:", age, "city:", city)
kw_func2('zuodw', 29, city = 'dalian')
#kw_func2('zuodw', 29, job = 'dalian')



def func3(x, y = 2, *, city, **kw):
	print("x:", x, "y:", y, "kw:", kw, "city:", city)
	
func3(3, 5, city = "dalian", job="engineer")





#尾递归
def fact(x, total = 1):
	if(x == 1):
		return total
	return fact(x - 1, x * total)

print(fact(5))

#TEST
def move(n, a, b, c):



	
	





