#encoding=utf-8
import os
from io import StringIO
import pickle
import json

""" IO """

""" 文件读写 """
current_path = os.getcwd()
# current_path = os.path.abspath('.')
file_path = os.path.join(current_path, 'bak.txt')
if os.path.exists(file_path):
    print('Error: %s is already exist' % (str(os.path.split(file_path)[1])))
else:
    pass
with open(file_path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)


file_path_test = os.path.join(current_path, 'test.txt')
if os.path.exists(file_path_test):
    print('Error: %s is already exist' % (str(os.path.split(file_path_test)[1])))
else:
    pass
with open(file_path, 'r', encoding='utf-8') as f:    
    with open(file_path_test, 'a+', encoding='utf-8') as ft:
        for line in f.readlines():
            ft.write(line)

def my_write():
    f = StringIO()
    f.write('Hello World')
    return f
def my_read():
    f = my_write()
    f.seek(2)
    print(f.read())
    print(f.getvalue())
    f.close()
my_read()


""" 操作文件和目录 """
print(os.name)
# print(os.uname()) windows has no uname()

print(os.listdir('.'))
file_list = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
print(file_list)

""" 序列化 """
d = dict(name='bob', age=20, scoree=88)
p1 = pickle.dumps(d)
print(p1)
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
p2 = pickle.loads(p1)
print(p2)

m_dict = dict(name='zuodw', age=29, scoree=98)
m_str = json.dumps(m_dict)
print('m_str: ', m_str)
d1 = json.loads(m_str)
print('d1:    ', d1)
with open('json.txt', 'w') as jf:
    json.dump(m_dict, jf)

with open('json.txt', 'r') as jf:
    print(json.load(jf))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

st = Student('zuodw', 29, 98)
""" 大多数class都有__dict__的属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。 """
m_str = json.dumps(st, default=lambda obj:obj.__dict__)
print(m_str)
def json2Student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(m_str, object_hook=json2Student))