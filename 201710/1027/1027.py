#/usr/bin/python

#coding: utf-8

import types

from types import MethodType

class Person(object):
	def __init__(self, name):
		self.__name = name

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def run(self):
		print(self.__name + '   RUN')

amy = Person('fanhx')
print(amy.getName())
amy.setName('zuodw')
print(amy.getName())
amy.run()


class Student(Person):
	def __init__(self, score):
		self.__score = score

	def getScore(self):
		return self.__score

	def setScore(self, score):
		self.__score = score

fanhx = Student(98)
print(fanhx.getScore())

# fanhx.run()

class Animal(object):
	def __init__(self):
		pass

	def run(self):
		print("Animal, run!!")

class Dog(Animal):
	def run(self):
		print("Dog, run!!")

	def __len__(self):
		return 100

class Cat(Animal):
	def run(self):
		print("Cat, run!!")

dog = Dog();
dog.run()

print(isinstance(dog, Animal), isinstance(dog, Dog), isinstance(dog, Cat))

animal = Animal()
animal.run()

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(dog)

print(type(animal))

print(type(run_twice) == types.FunctionType)

print(types.BuiltinFunctionType)

print(types.LambdaType)

print(types.GeneratorType)

print(isinstance(run_twice, types.FunctionType))

print(dir(dog))

print(len(dog))

fn = getattr(dog, 'run')

fn()


class Student(object):
	pass

s = Student()

s.name = 'zuodw'

def set_age(self, age):
	self.age = age

s.set_age = MethodType(set_age, s)

s.set_age(29)

print(s.age)

s2 = Student()

Student.set_age = MethodType(set_age, Student)

s2.set_age(2222)

print(s2.age)


class Person(object):
	pass


class Student(object):
	__slots__ = ('name', 'age')

s = Student()

s.name = 'zuodw'

s.age = 22

# s.score = 98

Student.name = 'zuodw'

Student.score = 22

s2 = Student()

print(s2.name)

print(hasattr(Student, 'score'))

# print(s.__dict__)

print(Student.__dict__)


class Person(object):
	pass


class Student(Person):
	count = 0
	books = []
	def __init__(self, name, age):
		self.name = name
		self.age = age
	pass


print(Student.__name__)
print(Student.__bases__)