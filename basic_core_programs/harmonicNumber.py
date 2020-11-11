"""
author -Maruti Bhosale
date -11-11-2020
time -18:35
package -basic_core_programs
Statement -Writing code for find Nth harmonic number

"""


def findHarmonicValue(n):
    harmonicValue = 0
    if n > 0:
        for num in range(1, n + 1):
            harmonicValue += 1 / num
    else:
        print("number should be greater than zero")
    return harmonicValue


harmonicNumber = int(input("Enter harmonic number: "))
if __name__ == "__main__":
    print(f"Harmonic value for number {harmonicNumber} is {findHarmonicValue(harmonicNumber)}")
