from collections import namedtuple
Point=namedtuple('Point',['x','y'])
q1=Point(1,2)
print(q1)

from collections import deque
q2=deque([1,2,3])
q2.appendleft(4)
print(q2)
q2.popleft()
print(q2)

from collections import defaultdict
q3=defaultdict(lambda:'huhucuo')
print(q3['2'])

from collections import Counter
c=Counter()
for ch in 'Huubang':
    c[ch]=c[ch]+1
print(c)

b=Counter('Huubang')
for key in b:
    print(key,b[key])

from collections import OrderedDict
od = OrderedDict()
od['a']=1
od['b']=2
od['c']=3
print(od)