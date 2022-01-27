class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hi I am {self.name} and I am {self.age} yo!")

    def talk(self):
        print(f"Bark!")


class Cat(Dog):

#Super is used in this case to get self.name and self.age directly from the Dog class
#The only thing we have to instance is the collor that doesnt exist in Dog
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

#If you define again the method in the child class, you'll overwrite the parent method
    def talk(self):
        print(f"Meoww!")

#General Class

class Veichle():

    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas

class Car(Veichle):

    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")


Sedan = Car(12000, 70, 'blue', 70)

print(Sedan.gas)
Sedan.emptyTank()
print(Sedan.gas)
Sedan.fillUpTank()
print(Sedan.gas)

class Truck(Veichle):

    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("Honk Honk")

jacare = Truck(200000, 100, 'Orange', 8)
jacare.beep()
print(jacare.tires)

