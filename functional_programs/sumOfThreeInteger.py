"""
author -Maruti Bhosale
date -11-11-2020
time -22:00
package -functional_programs
Statement -finding three number which adds to zero

"""


def sumToZero(array):
    """
    finding triplet whose addition is zero
    """

    length = len(array)
    for i in range(length - 2):
        for j in range(length - 1):
            for k in range(length):
                if array[i] + array[j] + array[k] == 0:
                    print(str(array[i]) + " + " + str(array[j]) + " + " + str(array[k]) + " = 0")


def createArray():
    """
    input array size and elements in array
    :return: return filled array
    """
    while True:
        try:
            size = int(input("Enter size of array: "))
            break
        except Exception as e:
            print(e)
    array = []
    for idx in range(size):
        while True:
            try:
                number = int(input("Enter number to add in array: "))
                break
            except Exception as e:
                print(e)
        array.append(number)
    return array


if __name__ == "__main__":
    filledArray = createArray()
    sumToZero(filledArray)
