"""
author -Maruti Bhosale
date -12-11-2020
time -16:30
package -functional_programs
Statement -finding distance between origin and given point

"""

import math

class EuclideanDistance:

    def __init__(self, x, y):  # define constructor
        """
        :param x: x-coordinator value
        :param y: y-coordinator value
        """
        self.x = x
        self.y = y

    def calculateDistance(self):  # calculating distance from origin to given point
        """
        :return:euclidean distance
        """
        distance = math.sqrt(self.x * self.x + self.y * self.y)

        return distance


while True:
    try:
        number1 = int(input("Enter x-coordinator: "))
        number2 = int(input("Enter y-coordinator: "))
        break
    except ValueError:
        print("Enter valid integer")


if __name__ == "__main__":
    euclideanDistance = EuclideanDistance(number1, number2)
    print(f"Euclidean Distance from origin to ({number1},{number2}) is {euclideanDistance.calculateDistance()}")
