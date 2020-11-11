"""
author -Maruti Bhosale
date -11-11-2020
time -22:00
package -functional_programs
Statement -finding three number which adds to zero

"""


def sumToZero(array):
    """finding triplet whose addition is zero"""

    length = len(array)
    for i in range(length - 2):
        for j in range(length - 1):
            for k in range(length):
                if array[i] + array[j] + array[k] == 0:
                    print(str(array[i]) + " + " + str(array[j]) + " + " + str(array[k]) + " = 0")


def createArray():
    """ for create and filled array """

    size = int(input("Enter size of array: "))
    array = []
    for idx in range(size):
        number = int(input("Enter number to add in array"))
        array.append(number)
    return array


if __name__ == "__main__":
    filledArray = createArray()
    sumToZero(filledArray)
