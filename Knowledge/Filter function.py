#Filter Function
#Filtering odd numbers 


def addSeven(x = 0):
    return x + 7

def isOdd(x):
    return x%2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

b = list (filter(isOdd, a)) #The filter func will use the function isOdd over the values in list a, if is odd
                            #the value will be appended to the list

c = list(map(addSeven, b)) #The filter and map function can be used togheter

print(a)
print(b)
print(c)