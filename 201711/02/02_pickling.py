#encoding=utf-8

""" 序列化和反序列化 : pickle """
import os
import json
import pickle

d = dict(name='bob', age=20, score=88)
# d = {'name':'bob', 'age':20, 'score':88}

print(pickle.dumps(d))

d = dict(name='zuodw', age=29, score=98)
print(d)
print(json.dumps(d))

class Student(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

st = Student('zuodw', 29)

def student2dict(student):
	return {
	'name' : student.name,
	'age' : student.age
	}
def dict2student(d):
	return Student(d['name'], d['age'])

# json.dumps(st)
# print(json.dumps(student2dict(st)))

json_str = json.dumps(st, default=lambda obj:obj.__dict__)

print(json_str)

js = json.loads(json_str, object_hook=dict2student)
print(js.name)