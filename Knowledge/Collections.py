#Collections 

import collections
from collections import Counter

#Containers 
#list
#set
#dict
#tuple - inmuttable

#Types
#1 counter 

c = Counter('Jaw')
#print(c)
d = Counter(['a', 'b', 'c' ,'d' , 'd'])
#print(d)
e = Counter({'a':1 , 'b':2})
#print(e)
f = Counter(cats = 4, dogs = 7)
#print(f)

#print(list(c.elements()))
#print(list(d.elements()))
#print(list(e.elements()))
#print(list(f.elements()))

#print(c.most_common(1))

#print(c.subtract(d))

cc = Counter(['a', 'a', 'b', 'c'])
dd = Counter({'a': 2, 'b': 3, 'c': 0})
#cc.subtract(dd)
#print(cc)
print(cc + dd)
print(cc - dd)
print(f"Intersection: {cc & dd}") #intersection 
print(f"Union: {cc | dd}") #union



#2 deque
#3 namedTuple()
#4 orderdDict
#5 defaultdict 
