"""
Name : Han Seokwon
Student ID : 2020180117
Description :  This moudle contains the ADT for Lab01
"""

from math import sqrt

class Functions:
    def getFactorial(self, n):
        if(n < 0):
            print("inaccurate input")
        elif(n == 0 or n == 1):
            return 1
        else:
            return n * self.getFactorial(n-1)

    def getTriples(self, bound):
        print("Pythagorean Triplets within {}".format(bound))
        for a in range(1, bound):
            for b in range(1, bound):
                for c in range(1, bound):
                    if(a**2 + b**2 == c**2):
                        print("{} {} {}".format(a, b, c ))

    def drawTriangles(self, lines):
        for line in range(1, lines + 1 ): # upper side triangle
            print(" " * (line - 1), end="")
            print("*" * (2 * lines + 1 - 2 * line))
        print()
        for line in range(lines + 1, 0, -1): # lower side triangle
            print(" " * (line - 1), end="")
            print("*" * (2 * lines + 1 - 2 * line))

class Complex:
    def __init__(self, x = 0.0 , y = 0.0):
        self.real = x
        self.imaginary = y

    def getReal(self):
        return self.real

    def getImaginary(self):
        return self.imaginary

    def __str__(self):
        return "({}, {}i)".format(self.real, self.imaginary)

    def __repr__(self):
        return "(real = {}, imaginary = {}i)".format(self.real, self.imaginary)

    def __add__(self, other):
        x = self.real + other.real
        y = self.imaginary + other.imaginary
        return Complex(x, y)

    def __sub__(self, other):
        x = self.real - other.real
        y = self.imaginary - other.imaginary
        return Complex(x, y)

    def __mul__(self, other):
        x = (self.real * other.real) - (self.imaginary * other.imaginary)
        y = (self.imaginary * other.real) + (self.real * other.imaginary)
        return Complex(x, y)

    def __abs__(self):
        x = self.real
        y = self.imaginary
        return (x*x + y*y)**(1/2)

class Point3D:
    def __init__(self, x = 0.0, y = 0.0, z = 0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({} , {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return "({} , {}, {})".format(self.x, self.y, self.z)

    def setCord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self): # return distance from current point to origin
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    def distance(self, p): # return distance from current point to other point
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2 + (self.z - p.z)**2)

    def translate(self, a, b, c):
        self.x += a
        self.y += b
        self.z += c

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def multiply(self, alpha): # scala multiply
        self.x *= alpha
        self.y *= alpha
        self.z *= alpha




