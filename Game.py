import random
from Board import *
from DisplayBoard import *

class Game:

    def __init__(self,player1, player2):
        self.board = DisplayBoard()
        self.players = [player1,player2]
        self.winner = None
        self.pTurn = random.randrange(2)
        self.isOver = False

#=== Functions

    def setWinner(self, winData):
        self.isOver = True
        self.winner = self.players[self.pTurn]

    def playTurn(self):
        spot = self.players[self.pTurn].chooseSpot()

        while (not self.board.isSpotFree(spot)): #if spot not free, we ask the player to pick a new one
            print("Spot is taken already, please choose another spot.")
            spot = self.players[self.pTurn].chooseSpot()

        self.board.updateSpot(spot, self.pTurn)

    def pTurnSwitch(self):
        self.pTurn = 1 * (1 - self.pTurn) # if pTurn = 1 => then pTurn = 1*(1-1) = 0, if pTurn = 0 => then pTurn = 1*(1-0) = 1*1 = 1 || switches between 0 and 1

    def playGame(self):
        print(self.players[self.pTurn].name + " starts the game.")
        while (not self.isOver):
            self.playTurn()

            winData = self.board.isWinner()
            if(winData):#if nobody is winning, winData = None
                self.setWinner(winData)


            self.pTurnSwitch()

            self.board.consoleDisplay()
        print(self.winner.name + " won the game.")


if __name__ == "__main__":
    from Player import *

    game = Game(Player('LnCol'), Player('Json'))

    game.playGame()