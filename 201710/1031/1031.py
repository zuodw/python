#/usr/bin/python3
#encoding=utf-8
'''
pets = ['dog', 'cat', 'bird', 'cat', 'rabbit','cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


#functions

def describe_pet(animal_type, pet_name):
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title())

describe_pet('dog', 'harry')

describe_pet(pet_name = 'harry', animal_type = 'dog')


def build_person(first_name, last_name):
    person = {'first':first_name, 'last':last_name}
    return person
print(build_person('zuo', 'dawei')

def greet_users(names):
    for name in names:
        print('Hello' + " " + name + '!')
    names.append('zdw')

names = ['zzz', 'fff', 'zuodw', 'fanhx']

greet_users(names[:])

print(names)
'''

def func(*args):
    #*args is a tuple
    print('args is a tuple')
    print(args)

func(1,2,3,4,5)


def build_profile(first, last, **kw):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in kw.items():
        profile[key] = value
    return profile

user_profile = build_profile('zuo', 'dawei', age = 29, score = 98)
print(user_profile)
