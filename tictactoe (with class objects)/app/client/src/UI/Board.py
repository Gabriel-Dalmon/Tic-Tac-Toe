import pygame

class Board:

    def __init__(self, container):
        self.container = container
        self.length =  2*(self.container.get_height() // 3)
        self.pos = (self.container.get_width() // 2 - self.length // 2,self.container.get_height() // 2 - self.length // 2) #the x,y position of the top left corner 
        
        self.resetBoard()
        self.casesRect = [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
                    ]
        self.initBoard()


    def resetBoard(self):
        self.cases = [
                    [None, None, None],
                    [None, None, None],
                    [None, None, None]
        ]
        
    def initBoard(self):
        rectPos = [self.pos[0],self.pos[1]]
        for row in range (3):
            for col in range (3):
                self.casesRect[row][col] = pygame.Rect(rectPos[0], rectPos[1],self.length//3,self.length//3)
                rectPos[1] += self.length//3
            rectPos = [rectPos[0] + self.length//3,self.pos[1]]



    def updateCase(self, coords, symbol):
        self.cases[coords[1]][coords[0]] = symbol #replaces a rectangle with a string "o" or "x"

    def drawBoard(self):
        pygame.draw.line(self.container,"white",(self.pos[0],self.container.get_height() // 2 - self.length // 6),(self.pos[0] + self.length,self.container.get_height() // 2 - self.length // 6),10)
        pygame.draw.line(self.container,"white",(self.pos[0],self.container.get_height() // 2 + self.length // 6),(self.pos[0] + self.length,self.container.get_height() // 2 + self.length // 6),10)
        pygame.draw.line(self.container,"white",(self.container.get_width() // 2 - self.length // 6,self.container.get_height() // 2 - self.length // 2),(self.container.get_width() // 2 - self.length // 6,self.container.get_height() // 2 + self.length // 2),10)
        pygame.draw.line(self.container,"white",(self.container.get_width() // 2 + self.length // 6,self.container.get_height() // 2 - self.length // 2),(self.container.get_width() // 2 + self.length // 6,self.container.get_height() // 2 + self.length // 2),10)




    def drawCross(self, centerPos):
        pygame.draw.line(self.container, "#1af4ba",(centerPos[0] - self.length // 8,centerPos[1] - self.length // 8),(centerPos[0] + self.length // 8,centerPos[1] + self.length // 8),10)
        pygame.draw.line(self.container, "#1af4ba",(centerPos[0] + self.length // 8,centerPos[1] - self.length // 8),(centerPos[0] - self.length // 8,centerPos[1] + self.length // 8),10)

    def drawCircle(self, centerPos):
        pygame.draw.circle(self.container, "#f41a54", centerPos, (self.length // 8))
        pygame.draw.circle(self.container, "#1a0033", centerPos, (self.length // 8 - 10))

    def drawSymbol(self, coords, type): #turns the table coords of the logic side of a symbol into the coords of the center where it should be drawn on the board
        xPos = self.pos[0] + self.length // 6 +(coords[0] * self.length // 3)
        yPos = self.pos[1] + self.length // 6 + (coords[1] * self.length // 3)
        if type == 1:
            self.drawCross((xPos,yPos))
        elif type == 0:
            self.drawCircle((xPos,yPos))

    def drawSymbols(self):
        for row in range(3):
            for col in range(3):
                self.drawSymbol((col,row),self.cases[col][row])

    def getCaseClicked(self, pos):
        for row in range(3):
            for col in range(3):
                if self.casesRect[col][row].collidepoint(pos):
                    return(row, col)
        return None