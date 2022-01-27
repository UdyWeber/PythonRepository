class Dog:
    #Usualy we define class variables at the top of the class
    #The class variables can be called simply calling the class . the name of the variable like Dog.dogs
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)


    def __str__(self):

        return f"{str(self.name)}"

    @classmethod #Decorator says what youre creating
    #You can use class methods to call a method without instancing the class
    #For example Dog.num_dogs
    #Cls = class name
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        """barks n times"""
        for _ in range(n):
            print("bark!")

jaw = Dog("Jaw")