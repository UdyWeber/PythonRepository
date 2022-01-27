#To change the value of a global variable into a local func we have to use
#The command global and after that the variable that we want to change

var = 9
loop = True
newVar = 23

def func(x):
    newVar = 7

    if x == 5:
        return newVar

def globalLocal(newVal):
     global newVar
     newVar = newVal

globalLocal(5)
print(newVar)
