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
        """
         calculating win and loss percentage
        :param countWin: count of win points
        :param countLoss: count of loss points
        :param countPlay: number of times play
        :return: win percentage and loss percentage
        """
        winPercentage = (countWin / countPlay) * 100
        lossPercentage = (countLoss / countPlay) * 100
        return winPercentage, lossPercentage

    def play(self):
        """
        :return: win count, loss count and number of played count
        """
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
        """
        taking inputs for gambling conditions
        """
        while True:
            try:
                self.stake = int(input("Enter money amount to start gambling: "))
                self.goal = int(input("Enter money amount for win: "))
                self.numberOfTimes = int(input("How many times want to play: "))
                if self.stake < 1 or self.goal < 1 or self.numberOfTimes < 1:
                    print("Enter numbers should be positive integer")
                    continue
                break
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    gambler = Gambler()
    gambler.setCondition()
    countWin, countLoss, countPlay = gambler.play()
    winPer, lossPer = gambler.findPercentage(countWin, countLoss, countPlay)
    print("Win Percentage: ", winPer)
    print("Loss Percentage: ", lossPer)
