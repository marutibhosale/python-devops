"""
author -Maruti Bhosale
date -16-11-2020
time -22:30
package -functional_programs
Statement -inserting and printing elements in 2d array

"""


class Array2D:

    def inputArrayParameters(self):
        """ taking input for 2d array from user for number of rows and columns and all elements in array"""

        try:
            numbersOfColumns = int(input("Enter number of columns: "))
            numbersOfRows = int(input("Enter number of rows: "))
        except Exception as e:
            print(e)
            self.inputArrayParameters()

        self.array = []
        for column in range(numbersOfColumns):
            rowElements = []
            for row in range(numbersOfRows):
                try:
                    element = int(input("Enter element in array: "))
                    rowElements.append(element)
                except Exception as e:
                    print(e)
                    self.inputArrayParameters()
            self.array.append(rowElements)

    def printArray(self):
        """printing array"""

        print(self.array)


if __name__ == "__main__":
    array2d = Array2D()
    array2d.inputArrayParameters()
    array2d.printArray()
