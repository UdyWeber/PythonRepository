#Self references to the instance youre calling
#Self references to the object youre linking it
#Like in the class, self references to Person and Person is instanced in Jaw

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Nice you created a Person! Are you god?')

    def introduce(self):
        print(f"Hi I am {self.name} and I have {self.age} years old!")

    def cussMartin(self):
        print(f"{self.name} says: Martin is a cunt face!")

    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight #It will apear as an error cause it wants to be identified, but we´re going to do that with the method

Jaw = Person('Jaw', 18)
Jaw.introduce()