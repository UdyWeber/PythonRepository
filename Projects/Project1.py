#Creating a class, adding class to an object, and adding the object to the list

objectList = []
loop = True

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Nice you've created a Person! Are you god?")

    def introduce(self):
        print(f"Hi I am {self.name} and I am {self.age} years old!")
        
    def change_age(self, age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight #It will apear as an error cause it wants to be identified, but we´re going to do that with the method

while True:

    def populateArray():

        i = 0

        while loop == True:

            name = str(input("Type the persons name: "))
            age = int(input("Type the persons age: "))

            global objectList
            person = Person(name, age)
            objectList.append(person)
            print(f"You added {objectList[i].name} to the list")
            i += 1

            exit = str(input('Continue?[Y/N]: '))

            while exit not in 'YyNn':

                exit = str(input('Continue?[Y/N]: '))

            if exit.upper() == 'N':

                break
    try:
        populateArray()

        break
    except:
        print('Something went wrong, tryagain!')

sizeArray = len(objectList)

for x in range(0, sizeArray):

    objectList[x].introduce()

