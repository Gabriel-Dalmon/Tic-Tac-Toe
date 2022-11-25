import pygame
from src.UI.Menu import *
import src.UI.Button as btn
import src.UI.Board as pgBoard
from src.Gameplay.Game import *
from ctypes import windll #uses Windows c functions to get the size of the monitor
import src.AI.TttAI as ai
import src.Online.Socket as socket

class Client:
    def __init__(self):
        self.gameStart = False
        #config = self.getConfig()
        self.theme = ("#1a0033","white")
        self.scores = [0,0]
        

        user32 = windll.user32
        self.win = pygame.init()
        self.win = pygame.display.set_caption('AG Games')
        self.screen = pygame.display.set_mode((user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)))
        pygame.display.flip()
        self.clock = pygame.time.Clock()
        self.mainMenuLoad()

    def mainMenuLoad(self):
        mainMenu = Menu(self.screen, ("SinglePlayer", self.singleplayerLoad),("Multiplayer", self.multiplayerLoad),("Options", self.optionsLoad),("Exit", self.quitClient))
        menuLoaded = True

        while menuLoaded:
            self.screen.fill(self.theme[0])
            for e in pygame.event.get():
                if e.type in [pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION]:
                    action = mainMenu.eventHandler(e.type, e.pos)
                    if action != None:
                        menuLoaded = False
            mainMenu.blitAll()
            self.clock.tick(24)     
            pygame.display.update()

        print("Load : ", action.__name__)
        action()


    def singleplayerLoad(self):
        board = pgBoard.Board(self.screen)
        game = Game("LnCol","Json")
        singleplayerLoaded = True
        font = pygame.font.Font('freesansbold.ttf', 32)

        while singleplayerLoaded:
            game.resetBoard()
            board.resetBoard()
            while game.isRunning:
                self.screen.fill(self.theme[0])
                board.drawBoard()
                backBtn = btn.Button("Back", self.mainMenuLoad, ('freesansbold.ttf', 32))
                backBtn.rect.center = (8 * self.screen.get_width() //10, 8 * self.screen.get_height() //10)
                backBtn.blitSelf(self.screen)

                caseClicked = None
                if(type(game.players[game.pTurn]) == ai.TttAI):
                    caseClicked = game.players[1].pickSpot(game.board.board, game.pTurn)
                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        caseClicked = board.getCaseClicked(e.pos)
                        if (backBtn.rect.collidepoint(e.pos)):
                            action = backBtn.command
                            game.isRunning = False
                            singleplayerLoaded = False
                            
                if caseClicked != None:
                    if(game.board.isSpotFree(caseClicked)):
                        board.updateCase(caseClicked, game.pTurn)
                    game.playGameClient(caseClicked)

                self.scoretext = [font.render("Score : " + str(game.players[0].score), True, "white"),font.render("Score : " + str(game.players[1].score), True, "white")]
                self.scoretextRect = [self.scoretext[0].get_rect(),self.scoretext[1].get_rect()] 
                self.scoretextRect[1].center = (self.screen.get_width()//12,self.screen.get_height()//8)
                self.scoretextRect[0].center = (self.screen.get_width() - self.screen.get_width()//12,self.screen.get_height()//8)
                self.screen.blit(self.scoretext[0], self.scoretextRect[0])
                self.screen.blit(self.scoretext[1], self.scoretextRect[1])

                board.drawSymbols()
                self.clock.tick(30)     
                pygame.display.update()
            if singleplayerLoaded:
                if game.winType == "draw":
                    text = font.render("It's a Draw !", True, "white")
                else:
                    text = font.render(game.winner.name + " won the game !", True, "white")
                textRect = text.get_rect()
                textRect.center = (self.screen.get_width() // 2, self.screen.get_height() // 10)
                self.screen.blit(text, textRect)

                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        game.isRunning = True
                self.clock.tick(20)
                pygame.display.update()
        action()


    def multiplayerLoad(self):
        clientSocket = socket.Socket()
        clientSocket.socket.sendMsg("LnCol")
        board = pgBoard.Board(self.screen)
        game = Game("LnCol","Json")
        multiplayerLoaded = True
        font = pygame.font.Font('freesansbold.ttf', 32)
        

        while multiplayerLoaded:
            self.screen.fill(self.theme[0])
            board.drawBoard()
            caseClicked = None

            instruction = clientSocket.recvMsg()
            if type(instruction) == "getCoord":
                for e in pygame.event.get():
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        caseClicked = board.getCaseClicked(e.pos)
                        if caseClicked != None:
                            if(game.board.isSpotFree(caseClicked)):
                                clientSocket.sendMsg(caseClicked)
                                board.updateCase(caseClicked, game.pTurn)

            self.scoretext = [font.render("Score : " + str(game.players[0].score), True, "white"),font.render("Score : " + str(game.players[1].score), True, "white")]
            self.scoretextRect = [self.scoretext[0].get_rect(),self.scoretext[1].get_rect()] 
            self.scoretextRect[1].center = (self.screen.get_width()//12,self.screen.get_height()//8)
            self.scoretextRect[0].center = (self.screen.get_width() - self.screen.get_width()//12,self.screen.get_height()//8)
            self.screen.blit(self.scoretext[0], self.scoretextRect[0])
            self.screen.blit(self.scoretext[1], self.scoretextRect[1])
            board.drawSymbols()
            self.clock.tick(30)     
            pygame.display.update()

            if instruction == "draw":
                text = font.render("It's a Draw !", True, "white")
            else: 
                text = font.render(instruction + " won the game !", True, "white")
            textRect = text.get_rect()
            textRect.center = (self.screen.get_width() // 2, self.screen.get_height() // 10)
            self.screen.blit(text, textRect)


    def optionsLoad(self):
        print("OptionsLoad")

    def winRouter(self):
        
        while True:

            self.clock.tick(30)

    def quitClient(self):
        pygame.quit()
        quit()

    def noAction(self):
        pass


if __name__ == "__main__":
    client = Client()