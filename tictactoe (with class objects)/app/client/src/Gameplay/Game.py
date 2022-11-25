import random
from src.Gameplay.Board import *
from src.Gameplay.Player import *
from src.AI.TttAI import *

class Game:

    def __init__(self,player1, player2):
        self.players = [Player(player1),TttAI(player2)]
        self.resetBoard()
        self.isRunning = True
        self.winner = None

    def resetBoard(self):
        self.board = Board()
        self.pTurn = random.randrange(2)
        
        

#=== Functions

    def setWinner(self, winInfo):
        self.isRunning = False
        self.winner = self.players[self.pTurn]
        self.winner.score += 1
        self.winType = winInfo

    def playTurn(self):
        spot = self.players[self.pTurn].chooseSpot()

        while (not self.board.isSpotFree(spot)): #if spot not free, we ask the player to pick a new one
            print("Spot is taken already, please choose another spot.")
            spot = self.players[self.pTurn].chooseSpot()

        self.board.updateSpot(spot, self.pTurn)

    def pTurnSwitch(self):
        self.pTurn = 1 * (1 - self.pTurn) # if pTurn = 1 => then pTurn = 1*(1-1) = 0, if pTurn = 0 => then pTurn = 1*(1-0) = 1*1 = 1 || switches between 0 and 1

    def playGameClient(self, casePicked):
        if(self.board.isSpotFree(casePicked)):#if the case is free, then update logic and engine board
            self.board.updateSpot(casePicked, self.pTurn)
            self.players[1].updateBoard(casePicked,self.pTurn)
            #self.memory[0].updateCase(casePicked, self.memory[1].pTurn)
            winInfo = self.board.isWinner()

            if(winInfo):
                self.setWinner(winInfo)
            self.pTurnSwitch()
            
    

    def playGame(self):
        print(self.players[self.pTurn].name + " starts the game.")
        while (not self.isRunning):
            self.playTurn()

            winInfo = self.board.isWinner()
            if(winInfo):
                self.setWinner(winInfo)


            self.pTurnSwitch()

            self.board.consoleDisplay()
        print(self.winner.name + " won the game.")


if __name__ == "__main__":
    
    game = Game("LnCol", "Json")
    game.playGame()