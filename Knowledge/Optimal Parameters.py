def func(x = 1):

    return x ** 2

#call = func()

def wordFreeq(word , add = 5, freq = 1):

    print((word + ' ')*(freq+ add))

#call2 = wordFreeq('Jaw', 5)

#Now with a class

class car(object):

    def __init__(self, brand, model, year, condition = 'New', kms = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll = True):

        if showAll:
            print(f"This car is a {self.brand} {self.model} from {self.year}, it is {self.condition} and has {self.kms} kms.")
        else:
            print(f"This car is a {self.brand} {self.model} from {self.year}")

car = car('Ford', 'Fusion', 2012)
car.display(False)