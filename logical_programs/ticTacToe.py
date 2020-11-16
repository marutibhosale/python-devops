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
        self.gameBoard = [[' ', '|', ' ', '|', ' '],
                          ['-', '+', '-', '+', '-'],
                          [' ', '|', ' ', '|', ' '],
                          ['-', '+', '-', '+', '-'],
                          [' ', '|', ' ', '|', ' ']]

    def printBoard(self):
        for row in self.gameBoard:
            print('\n')
            for item in row:
                print(item, end='')

    def playUser(self):
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
        symbol = ' '
        if player == 'user':
            symbol = 'X'
            self.userPosition.append(pos)
        elif player == 'cpu':
            symbol = '0'
            self.cpuPosition.append(pos)

        if pos == 1:
            self.gameBoard[0][0] = symbol
        elif pos == 2:
            self.gameBoard[0][2] = symbol
        elif pos == 3:
            self.gameBoard[0][4] = symbol
        elif pos == 4:
            self.gameBoard[2][0] = symbol
        elif pos == 5:
            self.gameBoard[2][2] = symbol
        elif pos == 6:
            self.gameBoard[2][4] = symbol
        elif pos == 7:
            self.gameBoard[4][0] = symbol
        elif pos == 8:
            self.gameBoard[4][2] = symbol
        elif pos == 9:
            self.gameBoard[4][4] = symbol

    def checkWinner(self):
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

