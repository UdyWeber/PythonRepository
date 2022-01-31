#Lambda function

def func(x = 0):
    func2 = lambda x: x+5

    return func2(x) + 85

func3 = lambda x, y : x + y

print(func3(5, 5))

#func2 = lambda x = 0: x+5 #Anonymous function

print(func(5))