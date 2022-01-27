import math

class Point():

    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):

        self.x += x
        self.y += y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, p):
        #Make add in class
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        #Make subtraction in class
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        #Make multiplication in class
        return self.x * p.x + self.y * p.y

    def __ge__(self, p):
        #Greather than or equal to
        return self.length() >= p.length()

    def __lt__(self, p):
        #Less then
        return self.length() < p.length()

    def __le__(self, p):
        #Less than or equal to
        return self.length() <= p.length()

    def __gt__(self, p):
        #Greather than
        return self.length() > p.length()

    def __eq__(self, p):

        return self.x == p.x and self.y == p.y

    def __str__(self):
        #You can define a output insted the terminal giving you the object where the class is instanced
        #Return without the __str__ method <__main__.Point object at 0x0000027FD3DC0D30>
        return f"({str(self.x)},{str(self.y)})"



p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

p6 = p1 * p3
p7 = p1 + p2

p8 = p1 > p2

print(p8)


print(p6)
print(p7)