from tkinter import *

class Player:

    def __init__(self, name):
        self.name = name
        self.initWindow()
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]


    def chooseSpot(self):
        x = int(input("X: "))
        y = int(input("Y: "))
        return (x,y)

    def initWindow(self):
        self.window = Tk()
        self.window.title("TicTacToe")
        self.window.attributes ('-fullscreen', True)
        headbar = Frame(self.window)
        
        self.gameGrid = Frame(self.window)
        
        delBtn = Button(headbar, text = 'X', fg="white", bg="red", bd=0, justify=CENTER, width = 5, relief = FLAT, command = self.window.destroy)
        delBtn.pack(anchor="ne")

        self.displayBoard()

        headbar.pack(anchor="ne")
        self.gameGrid.pack()

    def drawCase(self, row, col, content):
        btnTest = Button(self.gameGrid, text = content, fg="black", bg="white", width=15, height=15, justify=CENTER, relief = FLAT)
        btnTest.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=5)

    def displayBoard(self):
        displayedBoard = [
            ["x","x","x"],
            ["x","x","x"],
            ["x","x","x"]
        ]
        for row in range (len(self._board)):
            for col in range (len(self._board[row])):
                if (self._board[row][col] == 1):
                    displayedBoard[row][col] = "o"
                elif (self._board[row][col] == -1):
                    displayedBoard[row][col] = "x"
                self.drawCase(row, col,displayedBoard[row][col])
        print("",displayedBoard[0], "\n", displayedBoard[1], "\n", displayedBoard[2])