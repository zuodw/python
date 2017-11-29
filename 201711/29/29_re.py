#encoding=utf-8

import re

m = re.match('foo', 'foooo')
if m is not None:
    print(m.group())

s = re.search('foo', 'affooo')
if s:
    print(s.group())

bt = 'bat|bet|bit'
try:
    print(re.match(bt, 'bat').group())
    print(re.search(bt, 'He bit me').group())
    print(re.match(bt, 'He bit me').group())
    print(re.match(bt, 'blt').group())
except AttributeError as e:
    print("AttributeError")

