"""
author -Maruti Bhosale
date -12-11-2020
time -16:30
package -functional_programs
Statement -finding three number which adds to zero

"""
import random


class Gambler:

    def findPercentage(self, countWin, countLoss, countPlay):
        winPercentage = (countWin / countPlay) * 100
        lossPercentage = (countLoss / countPlay) * 100
        return winPercentage, lossPercentage

    def play(self):
        winCount = 0
        lossCount = 0
        playCount = 0
        startMoney = self.stake
        while 0 < startMoney < self.goal and playCount < self.numberOfTimes:
            rand = random.randint(0, 1)
            playCount += 1
            if rand == 0:
                startMoney = startMoney-1
                lossCount = lossCount + 1
            else:
                winCount = winCount + 1
                startMoney = startMoney + 1
        return winCount, lossCount, playCount

    def setCondition(self):
        try:
            self.stake = int(input("Enter money amount to start gambling: "))
            self.goal = int(input("Enter money amount for win: "))
            self.numberOfTimes = int(input("How many times want to play: "))
        except ValueError as e:
            print(e)
            self.setCondition()


if __name__ == "__main__":
    gambler = Gambler()
    gambler.setCondition()
    countWin, countLoss, countPlay = gambler.play()
    winPer, lossPer = gambler.findPercentage(countWin, countLoss, countPlay)
    print("Win Percentage: ", winPer)
    print("Loss Percentage: ", lossPer)
