"""
author -Maruti Bhosale
date -11-11-2020
time -16:25
package -basic_core_programs
Statement -find percentage of head and tail count

"""

import random


def flipPercentage():
    headCount = 0
    tailCount = 0
    numberOfTimesFlips = int(input("How many times wants to flip coin: "))
    if numberOfTimesFlips > 0:
        for flip in range(numberOfTimesFlips):
            rand = random.random()
            if float(rand) > 0.5:
                headCount += 1
            else:
                tailCount += 1
        headPercentage = (headCount / numberOfTimesFlips) * 100
        tailPercentage = (tailCount / numberOfTimesFlips) * 100
        print("Head Percentage is: ", headPercentage)
        print("Tail Percentage is: ", tailPercentage)
    else:
        print("number should be positive")
    return


if __name__ == "__main__":
    flipPercentage()
