"""
Name : Han Seokwon
Student ID : 2020180117
Description :  This module test the ABT/ Types(Data structure) defined in Lab01 Module
"""

from Lab01 import Functions , Complex, Point3D

def useFunctions(): # run Function class's methods
    f1 = Functions()
    n = 5;
    print("Factorial of = {} is {}".format( n , f1.getFactorial(n)))
    print("getTriples(10)")
    f1.getTriples(10)
    print("drawTriangles(4)")
    f1.drawTriangles(4)

def useComplex(): # run Complex class's methods
    z1 = Complex(1.5, 5.6)
    z2 = Complex(4.0, 3.7)
    print(z1)
    print(z2)
    print("{} = {} + {} ".format(z1 + z2, z1, z2))
    print("{} = {} - {} ".format(z2 - z1, z2, z1))
    print("{} = {} * {} ".format(z1 * z2, z1, z2))
    print("{} = |{}|".format(abs(z1), z1))

def usePoint3D():  # run Point3D class's methods
    p1 = Point3D()
    p1.setCord(4.6, 6.7, 9.0)
    p2 = Point3D(3.6, 2.3, 1.2)
    print("p1 = {}".format(p1))
    print("p2 = {}".format(p2))
    print("p1's legnth = {:.2f}".format(p1.length()))
    print("p2's legnth = {:.2f}".format(p2.length()))
    print("distance between p1 and p2 = {:.2f}".format(p1.distance(p2)))

def main():
    # useFunctions()
    # useComplex()
    usePoint3D()

if __name__ == "__main__":
    main()

















