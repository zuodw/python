#encoding=utf-8
import functools

'''
#装饰器
def log(*args):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('Call %s' % func.__name__)
            func(*args, **kw)
        return wrapper
    return decorator

@log()
def now():
    print('2017/10/31')

now()

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name(self):
        print('aaaaa')
        return self.name

    def getAge(self):
        return self.age


st = Student('fanhx', 30)

print(st.getAge())

# print(st.getName())

print(st.name)

#@property

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = ''

    @property
    def full_name(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, middle_name):
        self.middle_name = middle_name


zuodw = Person('zuo', 'dawei')

zuodw.full_name = 'God'

print(zuodw.full_name)

class Screen(object):
    # def __init__(self):
    #     self._width = 0
    #     self._height = 0
    #     self._resolution = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
'''


class Number(object):
    def __len__(self):
        return 666

n = Number()

print(len(n))
