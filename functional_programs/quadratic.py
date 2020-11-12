"""
author -Maruti Bhosale
date -12-11-2020
time -18:30
package -functional_programs
Statement -finding roots fo quadratic equation

"""
import math

class Quadratic:

    def __init__(self, a, b, c):
        """
        :param a:value for coefficient a
        :param b:value for coefficient b
        :param c:value for coefficient c
        """
        self.a = a
        self.b = b
        self.c = c

    def calculateDeltaValue(self):
        """
        :return: absolute value of delta term
        """
        deltaValue = self.b * self.b - 4 * self.a * self.c
        return abs(deltaValue)

    def calculateRoots(self):
        """
        :return:roots of quadratic equation
        """
        delta = (self.calculateDeltaValue())
        rootOne = (-self.b + math.sqrt(delta)) / (2 * self.a)
        rootTwo = (-self.b - math.sqrt(delta)) / (2 * self.a)
        return rootOne, rootTwo


try:
    aValue = int(input("Enter a value: "))
    bValue = int(input("Enter b value: "))
    cValue = int(input("Enter c value: "))
except ValueError:
    print("Enter valid integer")

if __name__ == "__main__":
    quadratic = Quadratic(aValue, bValue, cValue)
    root1, root2 = quadratic.calculateRoots()
    print(f"Roots of given quadratic equation is: {root1} and {root2}")
