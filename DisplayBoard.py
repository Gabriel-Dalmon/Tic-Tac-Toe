from Board import *

class DisplayBoard(Board):

    def __init__(self):
        super().__init__()





    

    # def drawCase(self, row, col, content):
    #     btnTest = Button(self.gameGrid, text = content, fg="black", bg="white", width=15, height=15, justify=CENTER, relief = FLAT)
    #     btnTest.grid(column=col+1, row=row+1, sticky=W, padx=5, pady=5)

    # def displayBoard(self):
    #     displayedBoard = [
    #         ["x","x","x"],
    #         ["x","x","x"],
    #         ["x","x","x"]
    #     ]
    #     for row in range (len(self._board)):
    #         for col in range (len(self._board[row])):
    #             if (self._board[row][col] == 1):
    #                 displayedBoard[row][col] = "o"
    #             elif (self._board[row][col] == -1):
    #                 displayedBoard[row][col] = "x"
    #             self.drawCase(row, col,displayedBoard[row][col])
    #     print("",displayedBoard[0], "\n", displayedBoard[1], "\n", displayedBoard[2])


    
        # self.nextPick = None


        # self.bgcolor = "#1a0033"
        # self.fcolor = "white"

        # self.root = Tk()
        # self.root.title("TicTacToe")
        # self.root.attributes ('-fullscreen', True)
        # self.root.config (bg = self.bgcolor)


        # self.headbar = Frame(self.root,bg = self.bgcolor)

        # delBtn = Button(self.headbar, text = 'X', fg = self.fcolor, bg = self.bgcolor, bd=0, justify=CENTER, width = 5, relief = FLAT, command = self.root.destroy)
        # delBtn.pack(side="right")
        
        # self.headbar.pack(side="top", fill="x")

        # self.content = Frame(self.root, bg = self.bgcolor)
        # self.spots = []
        # for row in range(3):
        #     for col in range(3):
        #         border = Frame(self.content, bg="white")
        #         btn = Button(border, text="-", fg=self.fcolor, bg=self.bgcolor, width=20, height=20, relief=FLAT, command = partial(self.setPick, row,col))
        #         self.spots.append(border.grid(row=row, column=col))
        #         btn.pack(padx=5,pady=5)
        # self.content.pack()
        
    # def setPick(self, row, col):
    #     self.nextPick = (row,col)
    #     print(self.nextPick)