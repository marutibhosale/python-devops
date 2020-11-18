"""
author -Maruti Bhosale
date -12-11-2020
time -16:30
package -functional_programs
Statement -finding distance between origin and given point

"""

import math

class EuclideanDistance:

    def __init__(self, x_coordinator, y_coordinator):
        """
        define constructor
        :param x_coordinator: x-coordinator value
        :param y_coordinator: y-coordinator value
        """
        self.x_coordinator = x_coordinator
        self.y_coordinator = y_coordinator

    def calculateDistance(self):  # calculating distance from origin to given point
        """
        calculate distance between origin to given point
        :return:euclidean distance
        """
        distance = math.sqrt(self.x_coordinator * self.x_coordinator + self.y_coordinator * self.y_coordinator)

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
