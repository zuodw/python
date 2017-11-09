#encoding=utf-8
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

""" namedtuple """
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)

""" deque """
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

""" defaultdick """
d = {'name': 'zuodw', 'age': 29}
print(d['name'])
# print(d['score'])
dd = defaultdict(lambda: 'N/A')
print(dd['score'])

""" OrderedDict """
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od = OrderedDict()
od['z'] = 3
od['x'] = 1
od['y'] = 2
print(od)

class LastUpdOrderedDict(OrderedDict):
    def init(self, capacity):
        super.__init__(self)
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

c1 = Counter('programming')
print(c1)
print(c1.most_common(3))