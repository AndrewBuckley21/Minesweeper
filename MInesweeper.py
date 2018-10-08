import random


class Minesweeper:

    def __init__(self, size):
        self.dim = size
        self.board = []
        for row in range(self.dim):
            rowHolder = []
            for column in range(self.dim):
                rowHolder.append(self.marker())
            self.board.append(rowHolder)

    def marker(self):
        if (random.randrange(1000) % self.dim) == 0:
            return '*'
        else:
            return ' '

    # displayBoard: Display the board to the screen in a format that matches the examples given.
    def dividerLine(self):
        print("----|", end="")
        for d in range(self.dim):
            print("---|", end="")
        print()

    def displayBoard(self, hide=False):
        # Print initial row of letters
        print("      ", end="")
        for add in range(self.dim):
            print(chr(ord('A') + add), end=" | ")
        print()
        # Print first divider line
        self.dividerLine()
        # Print all of the rows followed by a divider line
        for row in range(self.dim):
            # Print the row number
            if row >= 10:
                print("", row, end=" | ")
            else:
                print(" ", row, end=" | ")
                # Print the row
            for column in range(self.dim):
                if hide and self.board[row][column] == '*':
                    print(" ", end=" | ")
                else:
                    print(self.board[row][column], end=" | ")
            print()
            # Print the divider line
            self.dividerLine()

    # makeMove: Determine if the move landed on a mine. Returns 'True' if a mine was not landed on.
    def makeMove(self, move):
        combinedMove = move.split(',')
        column = ord(combinedMove[0]) - 65
        row = int(combinedMove[1])
        if (column >= self.dim) or (column < 0) or (row >= self.dim) or (row < 0):
            print("Move \"", move, "\" is out of range", sep="")
            return True
        elif self.board[row][column] == '*':
            print("*****************************")
            print("******** B O O M ! **********")
            print("*****************************")
            return False
        else:
            self.board[row][column] = str(self.calcNum(row, column))
            return True

    # winner: determines if the player has won the game.
    def winner(self):
        listAll = []
        for row in range(len(self.board)):
            for column in range(len(self.board)):
                listAll.append(self.board[row][column])
        if ' ' not in listAll:
            print("***********************************")
            print("********** W I N N E R ! **********")
            print("***********************************")
            return True
        else:
            return False

    def calcNum(self, moveRow, moveCol):
        num = 0
        if moveCol != 0:
            if self.board[moveRow][moveCol - 1] == '*':
                num += 1

        try:
            if self.board[moveRow][moveCol + 1] == '*':
                num += 1
        except IndexError:
            num += 0

        if moveRow != 0:
            if moveCol != 0:
                if self.board[moveRow - 1][moveCol - 1] == '*':
                    num += 1
            if self.board[moveRow - 1][moveCol] == '*':
                num += 1
            try:
                if self.board[moveRow - 1][moveCol + 1] == '*':
                    num += 1
            except IndexError:
                num += 0
        if moveCol != 0:
            try:
                if self.board[moveRow + 1][moveCol - 1] == '*':
                    num += 1
            except IndexError:
                num += 0
        try:
            if self.board[moveRow + 1][moveCol] == '*':
                num += 1
        except IndexError:
            num += 0
        try:
            if self.board[moveRow + 1][moveCol + 1] == '*':
                num += 1
        except IndexError:
            num += 0

        return num


def main():
    size = int(input("What size board do you want (3-15, enter 0 to stop)? "))
    print(size)
    if (size > 2) and (size < 16):
        game = Minesweeper(size)
        game.displayBoard(hide=True)
        move = "not empty"
        while move != "":
            move = input("Enter coordinate (e.g. \"A,15\") or empty string to stop: ")
            print(move)
            print()
            if len(move) > 0:
                if game.makeMove(move):
                    if game.winner():
                        game.displayBoard(hide=False)
                        break
                    else:
                        game.displayBoard(hide=True)
                else:
                    game.displayBoard(hide=False)
                    break
    elif (size < 0) or (size in [1, 2]) or (size > 15):
        print("Please pay attention!")


if __name__ == "__main__":
    main()

