"""
author -Maruti Bhosale
date -12-11-2020
time -18:30
package -functional_programs
Statement -finding roots fo quadratic equation

"""
import math

class Quadratic:

    def __init__(self, coefficient_a, coefficient_b, coefficient_c):
        """
        initializing constructor
        :param coefficient_a:value for coefficient a
        :param coefficient_b:value for coefficient b
        :param coefficient_c:value for coefficient c
        """
        self.coefficient_a = coefficient_a
        self.coefficient_b = coefficient_b
        self.coefficient_c = coefficient_c

    def calculateDeltaValue(self):
        """
        calculating delta value
        :return: absolute value of delta term
        """
        deltaValue = self.coefficient_b * self.coefficient_b - 4 * self.coefficient_a * self.coefficient_c
        return abs(deltaValue)

    def calculateRoots(self):
        """
        finding roots of quadratic equation
        :return:roots of quadratic equation
        """
        delta = (self.calculateDeltaValue())
        rootOne = (-self.coefficient_b + math.sqrt(delta)) / (2 * self.coefficient_a)
        rootTwo = (-self.coefficient_b - math.sqrt(delta)) / (2 * self.coefficient_a)
        return rootOne, rootTwo


while True:
    try:
        aValue = int(input("Enter the value for coefficient a: "))
        bValue = int(input("Enter the value for coefficient b: "))
        cValue = int(input("Enter the value for coefficient c: "))
        break
    except ValueError:
        print("Enter valid integer")


if __name__ == "__main__":
    quadratic = Quadratic(aValue, bValue, cValue)
    root1, root2 = quadratic.calculateRoots()
    print(f"Roots of given quadratic equation is: {root1} and {root2}")
