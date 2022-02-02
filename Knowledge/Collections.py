#Collections 

import collections
from collections import Counter
from collections import namedtuple


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
#print(cc + dd)
#print(cc - dd)
#print(f"Intersection: {cc & dd}") #intersection 
#print(f"Union: {cc | dd}") #union

#2 deque
#3 namedTuple()

#namedtuple functioning is like a class Where you instance that class in an object like Point
#and instance that object in a variable with the parameters

Point = namedtuple('Point', {'x':0, 'y':0, 'z':0}) #in the parameters you can use any iterable objects
Words = namedtuple('Words', 'a b c')
newP = Point(3,4,5)
print(newP[1])
print(newP._asdict())
print(newP._fields)

#To change a value into that tuple, we have to use the ._replace() in a bit different way 
#We have to overwrithe newP with the newP with the value we want to replace

# Wrong / newP._replace(y=8)
# Right:
newP = newP._replace(y=8)
print(newP)

#p2 = Point._make(['a', 'b', 'c'])
p2 = Words('A', 'B', 'C')
print(p2)

#4 orderdDict
#5 defaultdict 
