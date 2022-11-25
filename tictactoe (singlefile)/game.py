from random import randrange, choice

def consoleDisplay(board, player):
    displayBoard = [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
        ]
    for row in range(0,3) :
        for col in range(0,3):
            if(board[row][col] == 1):
                displayBoard[row][col] = "x"
            elif(board[row][col] == -1):
                displayBoard[row][col] = "o"

    print(player,"'s turn !\n",displayBoard[0][0], "|",displayBoard[0][1], "|", displayBoard[0][2], "\n",
        "-", "|","-", "|","-","\n",
        displayBoard[1][0], "|",displayBoard[1][1], "|",displayBoard[1][2],"\n",
        "-", "|","-", "|","-","\n",
        displayBoard[2][0], "|",displayBoard[2][1], "|",displayBoard[2][2]    
    )


def getPlayableSpots(board):
    spots = []
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == 0:
                spots.append((row,col))
    return spots

def getCorners(spots):
    cornersList = []
    for spot in spots:
        if spot in [(0,0),(2,0),(2,2),(0,2)]:
            cornersList.append(spot)
    return cornersList

def getOppositCorner(corner):
    newCorner = [None,None]
    for i in range (len(corner)):
        if corner[i] == 2:
            newCorner[i] = 0
        else:
            newCorner[i]=2
    return (newCorner[1],newCorner[0])

def linesSum(condition,board): #compares the sum of each lines with the parameter "condition", returns a list of each line
    lDiagSum = board[0][0] + board[1][1] + board[2][2] #Diagonal starting top left
    rDiagSum = board[0][2] + board[1][1] + board[2][0] #Diagonal starting top right
    if(lDiagSum in condition):
        return ("diag",0)
    elif(rDiagSum in condition):
        return ("diag",2)
    else:
        for i in range(0,3):
            rowSum = sum(board[i])
            colSum = board[0][i] + board[1][i] + board[2][i]
            if (rowSum in condition):
                return ("row",i)
            elif(colSum in condition):
                return ("col",i)
    return None

def chooseSpot(player, board, pTurn, turn, spotsLog):
    if player == "CPU":
        spots = getPlayableSpots(board)
        conditions = [[2*(1 + (pTurn * -2))],[2*(1 + (pTurnSwitch(pTurn) * -2))]] #conditions[[victoire],[defaite]] each condition is a single element list to be iterable for the linesSum function
        for condition in conditions:
            line = linesSum(condition,board) #("row",1)
            if(line != None):
                if(line[0] == "row"):
                    for i in range (0,3):
                        if(board[line[1]][i] == 0):
                            return (i,line[1])
                elif(line[0] == "col"):
                    for i in range (0,3):
                        if(board[i][line[1]] == 0):
                            return (line[1],i)
                else:
                    for i in range (0,3):
                        if(line[1] == 0):
                            if(board[i][i] == 0):
                                return (i,i)
                        elif(line[1] == 2):
                            if(board[i][2-i] == 0):
                                return (2-i,i)
        
        corners = getCorners(spots)

        #when CPU plays first
        if(turn == 1):
            corner = choice(corners)
            return (corner[1], corner[0])
        elif(turn == 3):
            if(len(corners) == 2):
                corner = choice(corners)
                return (corner[1], corner[0])
            elif(board[1][1] != 0):
                if(spotsLog[pTurn][0][0] == 0):
                    return(0,1)
                else:
                    return(2,1)
            elif((board[1][1] == 0) and (len(corners) == 3)): #if the player picks a cross extremity at his first turn
                    if(spotsLog[pTurnSwitch(pTurn)][0][1] != 1 ): #if this pick isn't on the middle line
                        if(spotsLog[pTurn][0][1] == 2): # and if 
                            return (spotsLog[pTurn][0][0],0)
                        else:
                            return (spotsLog[pTurn][0][0],2)
                    else:
                        if(spotsLog[pTurn][0][0] == 2):
                            return (0,spotsLog[pTurn][0][1])
                        else:
                            return (2,spotsLog[pTurn][0][1])
        elif(turn == 5):
            print(spots)
            if(len(corners) == 1): #if all the 3 corners were taken
                return (corners[0][1],corners[0][0]) #then pick last one
            elif(spotsLog[pTurnSwitch(pTurn)][0] in [(1,0),(2,1),(1,2),(0,1)]): #if opponent played one of the cross extremities at his first turn
                return (1,1) #then pick center
        
        #when CPU doesn't play first
        elif(turn == 2):
            if(spotsLog[pTurnSwitch(pTurn)][0] in [(0,0),(2,0),(2,2),(0,2)]): #if opponent played in a corner turn 1
                return (1,1)
            elif(spotsLog[pTurnSwitch(pTurn)][0] in [(1,0),(2,1)]): #if a player played in one of two of the cross extremities not opposed
                return (2,0)
            elif(spotsLog[pTurnSwitch(pTurn)][0] in [(1,2),(0,1)]): #if a player played in one of the two other of the cross extremities not opposed
                return (0,2)
            elif(board[1][1] != 0): #if opponent took center
                corner = choice(corners)
                return (corner[1], corner[0])

        elif(turn == 4):
            if(spotsLog[pTurnSwitch(pTurn)][0] in [(0,0),(2,0),(2,2),(0,2)]): #if the player had taken a corner as first move
                if(sum(board[1]) != 0):
                    return (0,1)
                else:
                    return (1,0)
            elif(spotsLog[pTurnSwitch(pTurn)][0] == (1,1)): #if the player had first taken center and that he took as the second move the opposit corner to the one the CPU had taken
                corner = choice(corners)
                return (corner[1], corner[0])
            elif(((spotsLog[pTurnSwitch(pTurn)][0][0] == spotsLog[pTurnSwitch(pTurn)][1][0]) or (spotsLog[pTurnSwitch(pTurn)][0][1] == spotsLog[pTurnSwitch(pTurn)][1][1])) and board[1][1] == 0): #if a player takes first one cross case and then the corner left next to his previous pick
                corners.remove(getOppositCorner(spotsLog[pTurn][0]))
                return (corners[0][1], corners[0][0])
            elif(board[1][1] == 0):
                return (1,1)
            

        randomSpot = choice(spots)
        print("randomMove")
        return (randomSpot[1],randomSpot[0])

    else: #player/not CPU
        try:
            x = int(input("X: "))
            y = int(input("Y: "))
            if (x < 0) or (x > 2) or (y < 0) or (y > 2):
                raise Exception   
        except:
            print("Please select correct coordinates, must be an integer number between 0 and 2 (both included), can't be a chain of characters or empty.")
            x, y = chooseSpot(player, board, pTurn, turn, spotsLog)     
        return (x,y)

def updateSpot(coords, board, pTurn):
    board[coords[1]][coords[0]] = 1 + (pTurn * -2) #if opposer = 0 then case = 1 | if opposer = 1 then case = -1

def isSpotFree(coords,board): #checks if the spot is free to be taken by a player
    if(board[coords[1]][coords[0]] == 0):
        return True

def isWinner(board): #if Win Condition is verified, then return win type and index of row, col or diag.
    winData = linesSum([3,-3],board)
    return winData

def pTurnSwitch(pTurn):
    pTurn = 1 * (1 - pTurn) # if pTurn = 1 => then pTurn = 1*(1-1) = 0, if pTurn = 0 => then pTurn = 1*(1-0) = 1*1 = 1 || switches between 0 and 1
    return pTurn

def playTurn(board, pTurn, player,turn, spotsLog):
    spot = chooseSpot(player, board, pTurn, turn, spotsLog)

    while (not isSpotFree(spot,board)): #if spot not free, we ask the player to pick a new one
        print(spot,"Spot is taken already, please choose another spot.",board)
        spot = chooseSpot(player, board, pTurn,turn, spotsLog)
    updateSpot(spot, board, pTurn)
    return spot

def playGame():
    board = [ 
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

    players = ["Player","CPU"]
    winner = None
    pTurn = randrange(2)
    isOver = False
    turn = 1
    spotsLog = [[],[]]


    print(players[pTurn] + " starts the game.")

    while (not isOver):
        spot = playTurn(board, pTurn, players[pTurn],turn, spotsLog)
        spotsLog[pTurn].append(spot)

        isOver = isWinner(board)
        if(len(getPlayableSpots(board)) == 0):
            isOver = 1
        

        consoleDisplay(board, players[pTurn])
        turn +=1
        pTurn = pTurnSwitch(pTurn)

    winner = pTurnSwitch(pTurn)
    if(isOver != 1):
        print(players[winner] + " won the game !")
    else:
        print("Draw, nobody won !")

playGame()