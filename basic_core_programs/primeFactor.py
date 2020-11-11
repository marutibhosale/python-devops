"""
author -Maruti Bhosale
date -11-11-2020
time -17:25
package -basic_core_programs
Statement -find prime factors for given number

"""
import math


def findPrimeFactor(n):
    for num in range(2, int(math.sqrt(n))):
        if num == 2 or num % 2 != 0:
            while n % num == 0:
                print(num)
                n = n / num
    if n > 2:
        print(int(n))
    return


number = int(input("Enter the number: "))
if __name__ == "__main__":
    findPrimeFactor(number)
