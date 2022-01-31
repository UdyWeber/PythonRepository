#Static and Class Methods

class Person(object):
    
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod #cls = class name 
    def getPopulation(cls): #class method
        return cls.population

    @staticmethod #dont have acess to class name
    def isAdult(age): #static
        return age >= 18

    def display(self):
        print(f"{self.name} is {self.age} years old")

newPerson = Person("jaw", 18)

print(Person.getPopulation())