"""
author -Maruti Bhosale
date -16-11-2020
time -22:34
package -functional_programs
Statement -inserting and printing elements in 2d array

"""


class Array2D:

    def inputArrayParameters(self):
        """ taking input for 2d array from user for number of rows and columns and all elements in array
        :return: array with filled all elements
        """
        while True:
            try:
                numbersOfColumns = int(input("Enter number of columns: "))
                numbersOfRows = int(input("Enter number of rows: "))
                if (numbersOfColumns or numbersOfRows) < 1:
                    print("number of rows and columns should be positive integer")
                    continue
                break
            except Exception as e:
                print(e)

        array = []
        for column in range(numbersOfColumns):
            rowElements = []
            for row in range(numbersOfRows):
                try:
                    element = int(input("Enter element in array: "))
                    rowElements.append(element)
                except Exception as e:
                    print(e)
                    self.inputArrayParameters()
            array.append(rowElements)
        return array

    def printArray(self, array):
        """printing array"""
        print(array)


if __name__ == "__main__":
    array2d = Array2D()
    array = array2d.inputArrayParameters()
    array2d.printArray(array)
