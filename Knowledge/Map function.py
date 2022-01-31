#Map Function

li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

print(list(map(func, li))) #apply the function that we pass as paramether to all the itens on the list without using a for loop

print([func(x) for x in li])