#Using lambda with Map and Filter function

a = [1,2,3,4,5,6,7,8,9,10]

newList = list(map(lambda x: x+5, a))
newEvenList = list(filter(lambda x: x % 2 == 0, a))
print(newList)
print(newEvenList)