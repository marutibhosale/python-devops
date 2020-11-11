"""
author -Maruti Bhosale
date -11-11-2020
time -18:00
package -basic_core_programs
Statement -Printing table for power of two

"""


def powerOfTwo(n):
    if 0 <= n < 31:
        for num in range(n+1):
            print("Square of {0} is {1} ".format(num, num**2))
    else:
        print("number should be in range of 0 to 30")
    return


number = int(input("Enter the number: "))
powerOfTwo(number)
