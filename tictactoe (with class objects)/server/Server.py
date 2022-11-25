import Gameplay.Game  as g
import Socket as s

class Server:
    def __init__(self):
        self.socket = s.Socket()
        player0 = self.socket.recvMsg(self.socket.socketsList[0][0])
        player1 = self.socket.recvMsg(self.socket.socketsList[1][0])
        self.game = g.Game(player0,player1[1])


    def playGame(self):
        while True:
            self.socket.sendMsg(self.socketsList[self.game.pTurn][0], "getCoord")
            coords = self.socket.recvMsg(self.socketsList[self.game.pTurn][0])
            if self.game.board.isSpotFree(coords):
                self.game.board.updateSpot(coords)
                self.socket.sendMsg(self.socketsList[self.game.pTurnSwitch(self.game.pTurn)][0], coords)
                winType = self.game.board.isWinner()
                if winType:
                    self.game.setWinner(winType)

if __name__ == "__main__":
    pass