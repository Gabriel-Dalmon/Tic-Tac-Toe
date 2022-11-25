class Board:

    def __init__(self):
        #board is the board interpretated by the computer. 0 = empty case. Both player's claims are differenciated with 1 and -1
        self.board = [ 
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    def getPlayableSpots(self):
        spots = []
        for row in range(0,3):
            for col in range(0,3):
                if self.board[row][col] == 0:
                    spots.append((row,col))
        return spots 

    def consoleDisplay(self):
        print(self.board[0], "\n",self.board[1],"\n",self.board[2])

    def isSpotFree(self, coords): #checks if the spot is free to be taken by a player
        if(self.board[coords[1]][coords[0]] == 0):
            return True

    def isWinner(self): #if Win Condition is verified, then return win type and index of row, col or diag.
        winCond = [3,-3] #the winCond is verified if the sum of a row, col, diag is equal to 3 or -3.

        lDiagSum = self.board[0][0] + self.board[1][1] + self.board[2][2] #Diagonal starting top left
        rDiagSum = self.board[0][2] + self.board[1][1] + self.board[2][0] #Diagonal starting top right
        if(lDiagSum in winCond):
            return ("diag",0)
        elif(rDiagSum in winCond):
            return ("diag",1)
        else:
            for i in range(0,3):
                rowSum = sum(self.board[i])
                colSum = self.board[0][i] + self.board[1][i] + self.board[2][i]
                if (rowSum in winCond):
                    return ("row",i)
                elif(colSum in winCond):
                    return ("col",i)
        if(len(self.getPlayableSpots()) == 0):
            return "draw"
        return None

    def updateSpot(self, coords, opposer):
        self.board[coords[1]][coords[0]] = 1 + (opposer * -2) #if opposer = 0 then case = 1 | if opposer = 1 then case = -1

