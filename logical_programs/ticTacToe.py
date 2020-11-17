"""
author -Maruti Bhosale
date -15-11-2020
time -
package -logical_programs
Statement -TicTacToc Game

"""
import random

class TicTacToe:
    userPosition = []
    cpuPosition = []

    def createBoard(self):
        """ creating game board"""
        self.gameBoard = [[' ' for _ in range(3)] for _ in range(3)]

    def printBoard(self):
        """printing game board"""
        for row in range(len(self.gameBoard)):
            print("\n______")
            for column in range(len(self.gameBoard)):
                print(str(self.gameBoard[row][column]), end='|')

    def playUser(self):
        """
        :return: return user new position
        """
        try:
            userPos = int(input("\n Enter your placement(1-9): "))
        except Exception as e:
            print(e)
            return self.playUser()
        while userPos in self.userPosition or userPos in self.cpuPosition:
            print("Position taken! Enter correct position")
            return self.playUser()
        if userPos < 1 or userPos > 9:
            print("position should be between 1-9")
            return self.playUser()
        return userPos

    def playCpu(self):
        """
        :return: return new cpu position
        """
        try:
            cpuPos = random.randint(1, 9)
        except Exception as e:
            print(e)
            return self.playCpu()
        while cpuPos in self.userPosition or cpuPos in self.cpuPosition:
            print("Position taken! Enter correct position")
            return self.playCpu()
        if cpuPos < 1 or cpuPos > 9:
            print("position should be between 1-9")
            return self.playCpu()
        return cpuPos

    def placePosition(self, player, pos):
        """ as per position inserting symbols in array"""
        symbol = ' '
        if player == 'user':
            symbol = 'X'
            self.userPosition.append(pos)
        elif player == 'cpu':
            symbol = '0'
            self.cpuPosition.append(pos)

        self.gameBoard[(pos - 1) // 3][(pos - 1) % 3] = symbol

    def checkWinner(self):
        """
         checking who is win the game
        :return: returns winning message
        """
        win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for condition in win:
            if set(condition).intersection(set(self.userPosition)) == set(condition):
                return "Congratulation you won!"
            elif set(condition).intersection(set(self.cpuPosition)) == set(condition):
                return "Cpu won!"
            elif len(self.cpuPosition)+len(self.userPosition) == 9:
                return "No empty Space to move"
        return ""


if __name__ == "__main__":
    tictactoe = TicTacToe()
    tictactoe.createBoard()
    tictactoe.printBoard()
    while True:
        userpos = tictactoe.playUser()
        tictactoe.placePosition('user', userpos)
        winner = tictactoe.checkWinner()
        if len(winner) > 0:
            print(winner)
            tictactoe.printBoard()
            break
        print('\n')
        print('='*30)
        tictactoe.printBoard()
        cpupos = tictactoe.playCpu()
        tictactoe.placePosition('cpu', cpupos)
        winner = tictactoe.checkWinner()
        if len(winner) > 0:
            print(winner)
            tictactoe.printBoard()
            break
        print('\n')
        print('='*30)
        tictactoe.printBoard()
