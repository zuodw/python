
class UpFooMetaClass(type):
    def __new__(cls, name, bases, attrs):
        upperAttr = dict({k.upper(), v} for k, v in attrs.items())
        return type.__new__(cls, name, bases, upperAttr)



class Foo(object, metaclass=UpFooMetaClass):
    name = 'foo'

print(hasattr(Foo, 'name'))
print(hasattr(Foo, 'NAME'))