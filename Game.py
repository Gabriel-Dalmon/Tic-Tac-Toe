import random



class Game:

    def __init__(self,player1, player2):
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]
        self.players = [player1,player2]
        self.winner = None
        self.pTurn = random.randrange(2)
        self.isOver = False

#=== Display

    def displayBoard(self):
        print(self.board)

#=== Conditions
    def isSpotExisting(self, spot):
        return True

    def isSpotFree(self, coords): #checks if the case is free to be taken by a player && coords contains two values (x,y)
        if(self.board[coords[1]][coords[0]] == 0):
            return True

#=== Functions

    def setWinner(self, winType):
        self.isOver = True
        self.winner = self.players[self.pTurn]

    def checkWinCond(self): #if Win Condition is verified, call setWinner function that also passes the self.isOver to True
        winCond = [3,-3] #the winCond is verified if the sum of a row, col, diag is equal to 3 or -3, it means every case in the row, col or diag is equal to either 1, either -1
        lDiagSum = self.board[0][0] + self.board[1][1] + self.board[2][2] #Diagonal starting top left
        rDiagSum = self.board[0][2] + self.board[1][1] + self.board[2][0] #Diagonal starting top right
        if(lDiagSum in winCond):
            self.setWinner(("diag",0))
        elif(rDiagSum in winCond):
            self.setWinner(("diag",1))
        else:
            for i in range(0,3):
                rowSum = sum(self.board[i])
                colSum = self.board[0][i] + self.board[1][i] + self.board[2][i]
                if (rowSum in winCond):
                    self.setWinner(("row",i))
                elif(colSum in winCond):
                    self.setWinner(("col",i))

    def updateSpot(self, coords): #update the board with the last spot picked and adapt to the actual player
        self.board[coords[1]][coords[0]] = 1 + (self.pTurn * -2) #pTurn = à 1 ou 0, on différencie les joueurs sur le plateau avec 1 et -1

    def playTurn(self):
        spot = self.players[self.pTurn].chooseSpot()

        while ((self.isSpotExisting(spot)) and (not self.isSpotFree(spot))): #if spot not free, we ask the player to pick a new one
            print("Spot is taken already, please choose another spot.")
            spot = self.players[self.pTurn].chooseSpot()

        self.updateSpot(spot)

    def pTurnSwitch(self):
        self.pTurn = 1 * (1 - self.pTurn) # if pTurn = 1 => then pTurn = 1*(1-1) = 0, if pTurn = 0 => then pTurn = 1*(1-0) = 1*1 = 1 || switches between 0 and 1

    def playGame(self):
        print(self.players[self.pTurn].name + " starts the game.")
        while (not self.isOver):
            self.playTurn()

            self.checkWinCond()

            self.pTurnSwitch()

            self.displayBoard()
        print(self.winner.name + " won the game.")


if __name__ == "__main__":
    from Player import *

    game = Game(Player('LnCol'), Player('Json'))

    game.playGame()