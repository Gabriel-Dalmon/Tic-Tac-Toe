import src.Gameplay.Player as p
import random


class TttAI(p.Player):
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.spots = None
        self.spotsLog = [[],[]]
        self.turn = 1
        self.lSumInfo = None

    def getPlayableSpots(self,board):
        self.spots = []
        for row in range(0,3):
            for col in range(0,3):
                if board[row][col] == 0:
                    self.spots.append((row,col))

    def getCorners(self):
        cornersList = []
        for spot in self.spots:
            if spot in [(0,0),(2,0),(2,2),(0,2)]:
                cornersList.append(spot)
        return cornersList

    def getOppositCorner(self, corner):
        oppCorner = [None,None]
        for i in range (len(corner)):
            if corner[i] == 2:
                oppCorner[i] = 0
            else:
                oppCorner[i]=2
        return (oppCorner[1],oppCorner[0])

    def linesSum(self, condition, board):
        self.lSumInfo = None
        lDiagSum = board[0][0] + board[1][1] + board[2][2] #Diagonal starting top left
        rDiagSum = board[0][2] + board[1][1] + board[2][0] #Diagonal starting top right
        if(lDiagSum in condition):
            self.lSumInfo = ("diag",0)
        elif(rDiagSum in condition):
            self.lSumInfo = ("diag",2)
        else:
            for i in range(0,3):
                rowSum = sum(board[i])
                colSum = board[0][i] + board[1][i] + board[2][i]
                if (rowSum in condition):
                    self.lSumInfo = ("row",i)
                elif(colSum in condition):
                    self.lSumInfo = ("col",i)
                    

    def playerSwitch(self, player):
        player = 1 * (1 - player) # if pTurn = 1 => then pTurn = 1*(1-1) = 0, if pTurn = 0 => then pTurn = 1*(1-0) = 1*1 = 1 || switches between 0 and 1
        return player

    def pickSpot(self, board, player):#board and player to be able to read the board properly
        self.getPlayableSpots(board)
        conditions = [[2*(1 + (self.playerSwitch(player) * -2))],[2*(1 + (player * -2))]] #conditions[[victoire],[defaite]] each condition is a single element list to be iterable for the linesSum function
        casePicked = None
        for condition in conditions:
            self.linesSum(condition,board) #("row",1)
            if(self.lSumInfo != None):
                if(self.lSumInfo[0] == "row"):
                    for i in range (0,3):
                        if(board[self.lSumInfo[1]][i] == 0):
                            casePicked = (i,self.lSumInfo[1])
                elif(self.lSumInfo[0] == "col"):
                    for i in range (0,3):
                        if(board[i][self.lSumInfo[1]] == 0):
                            casePicked = (self.lSumInfo[1],i)
                else:
                    for i in range (0,3):
                        if(self.lSumInfo[1] == 0):
                            if(board[i][i] == 0):
                                casePicked = (i,i)
                        elif(self.lSumInfo[1] == 2):
                            if(board[i][2-i] == 0):
                                casePicked = (2-i,i)
        corners = self.getCorners()
        #when CPU plays first
        if casePicked == None:
            if(self.turn == 1):
                corner = random.choice(corners)
                casePicked = (corner[1], corner[0])
            elif(self.turn == 3):
                if(len(corners) == 2):
                    corner = random.choice(corners)
                    casePicked = (corner[1], corner[0])
                elif(board[1][1] != 0):
                    if(self.spotsLog[player][0][0] == 0):
                        casePicked = (0,1)
                    else:
                        casePicked = (2,1)
                elif((board[1][1] == 0) and (len(corners) == 3)): #if the player picks a cross extremity at his first turn
                        if(self.spotsLog[self.playerSwitch(player)][0][1] != 1 ): #if this pick isn't on the middle line
                            if(self.spotsLog[player][0][1] == 2): # and if 
                                casePicked = (self.spotsLog[player][0][0],0)
                            else:
                                casePicked = (self.spotsLog[player][0][0],2)
                        else:
                            if(self.spotsLog[player][0][0] == 2):
                                casePicked = (0,self.spotsLog[player][0][1])
                            else:
                                casePicked = (2,self.spotsLog[player][0][1])
            elif(self.turn == 5):
                if(len(corners) == 1): #if all the 3 corners were taken
                    casePicked = (corners[0][1],corners[0][0]) #then pick last one
                elif(self.spotsLog[self.playerSwitch(player)][0] in [(1,0),(2,1),(1,2),(0,1)]): #if opponent played one of the cross extremities at his first turn
                    casePicked = (1,1) #then pick center
            
            #when CPU doesn't play first
            elif(self.turn == 2):
                if(self.spotsLog[self.playerSwitch(player)][0] in [(0,0),(2,0),(2,2),(0,2)]): #if opponent played in a corner turn 1
                    casePicked = (1,1)
                elif(self.spotsLog[self.playerSwitch(player)][0] in [(1,0),(2,1)]): #if a player played in one of two of the cross extremities not opposed
                    casePicked = (2,0)
                elif(self.spotsLog[self.playerSwitch(player)][0] in [(1,2),(0,1)]): #if a player played in one of the two other of the cross extremities not opposed
                    casePicked = (0,2)
                elif(board[1][1] != 0): #if opponent took center
                    corner = random.choice(corners)
                    casePicked = (corner[1], corner[0])

            elif(self.turn == 4):
                if(self.spotsLog[self.playerSwitch(player)][0] in [(0,0),(2,0),(2,2),(0,2)]): #if the player had taken a corner as first move
                    if(sum(board[1]) != 0):
                        casePicked = (0,1)
                    else:
                        casePicked = (1,0)
                elif(self.spotsLog[self.playerSwitch(player)][0] == (1,1)): #if the player had first taken center and that he took as the second move the opposit corner to the one the CPU had taken
                    corner = random.choice(corners)
                    casePicked = (corner[1], corner[0])
                elif(((self.spotsLog[self.playerSwitch(player)][0][0] == self.spotsLog[self.playerSwitch(player)][1][0]) or (self.spotsLog[self.playerSwitch(player)][0][1] == self.spotsLog[self.playerSwitch(player)][1][1])) and board[1][1] == 0): #if a player takes first one cross case and then the corner left next to his previous pick
                    corners.remove(self.getOppositCorner(self.spotsLog[player][0]))
                    casePicked = (corners[0][1],corners[0][0])
                elif(board[1][1] == 0):
                    casePicked = (1,1)
                
            else:
                randomSpot = random.choice(self.spots)
                print("randomMove")
                casePicked = (randomSpot[1],randomSpot[0])
            
        return casePicked


    def updateBoard(self,  coords, player):
        self.spotsLog[player].append(coords)
        self.turn += 1
