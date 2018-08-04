''' Problem text:
Time for some fake graphics!
Let’s say we want to draw game boards that look like this:
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe).
Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).
Ask the user what size game board they want to draw, and draw it for them.
'''

class GameBoard:
    hLine = "---"
    vLine = "|"
    space = "   "
    def __init__(self, length=3, width=3):
        self.length = length
        self.width = width

    def printBoard(self):
        for i in range (0, self.width):
            self.printHorizontal()
            self.printVertical()
        self.printHorizontal()
        return

    def printHorizontal(self):
        for i in range (0, self.length):
            print(" " + self.hLine, end="")
        print(" ")
        return

    def printVertical(self):
        for i in range (0, self.width):
            print(self.vLine + self.space, end="")
        print(self.vLine)
        return


def main():
    boardSize = int(input("What size board would you like?\n"))
    userBoard = GameBoard(boardSize, boardSize)
    userBoard.printBoard()
    return

if __name__ == "__main__": main()
