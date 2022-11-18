from random import randrange, choice

def consoleDisplay(board):
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
    print("",displayBoard[0][0], "|",displayBoard[0][1], "|", displayBoard[0][2], "\n",
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

def notOpposit(spots):
    if((((1,0) in spots) and ((1,2) in spots)) or (((0,1) in spots) and ((2,1) in spots))):
        return False
    return True

def getCorners(spots):
    cornersList = []
    for spot in spots:
        if spot in [(0,0),(2,0),(2,2),(0,2)]:
            cornersList.append(spot)
    return cornersList

def getOppositCorner(corner):
    for i in range (len(corner)):
        if corner[i] == 2:
            corner[i]=0
        else:
            corner[i]=2
    return corner

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

def chooseSpot(player, board, pTurn, turn):
    if player == "CPU":
        spots = getPlayableSpots(board)
        pos = 1 + (pTurn * -2)
        enemiePos = 1 + (pTurnSwitch(pTurn) * -2)
        conditions = [[2*(1 + (pTurn * -2))],[2*(1 + (pTurnSwitch(pTurn) * -2))]] #conditions[[victoire],[defaite]] each condition is a single element list to be iterable for the linesSum function
        print(conditions)
        for condition in conditions:
            line = linesSum(condition,board) #("row",1)
            print(line)
            if(line != None):
                if(line[0] == "row"):
                    for i in range (0,3):
                        if(board[line[1]][i] == 0):
                            print(condition)
                            return (i,line[1])
                elif(line[0] == "col"):
                    for i in range (0,3):
                        if(board[i][line[1]] == 0):
                            print(condition)
                            return (line[1],i)
                else:
                    for i in range (0,3):
                        if(line[1] == 0):
                            if(board[i][i] == 0):
                                print(condition)
                                return (i,i)
                        elif(line[1] == 2):
                            if(board[i][2-i] == 0):
                                print(condition)
                                return (2-i,i)

        if(turn == 1):
            corner = choice(getCorners(spots))
            return corner
        if(turn == 3):
            if(board[0][0] == 0):
                untakenCorners = getCorners(spots).remove(getOppositCorner(corner))
                if(len(getCorners(spots)) == 1):
                    if (sum(board[corner[1]]) == 0):
                        untakenCorners.remove(())
                    return choice(untakenCorners)
                else:
                    return choice(untakenCorners)
            else():
                return getOppositCorner(corner) #if center taken by opponent, take opposit corner to the previously taken one
        


    #     print(turn)
    #     if(turn == 1):
    #         print("random corner")
    #         corner = (randrange(0,3,2),randrange(0,3,2))
    #         return (corner) #randomCorner
    #     elif(turn == 3):
    #         if(board[1][1] == enemiePos):
    #             #oppositCorner()
    #             if(board[0][0] == pos):
    #                 return (2,2)
    #             elif(board[2][2] == pos):
    #                 return (0,0)
    #             elif(board[0][2] == pos):
    #                 return (2,0)
    #             else:
    #                 return (0,2)
    #         else:
    #             return (choice(spots)) #randomCorner()

    #     elif(turn == 4 and noCornerTaken(spots) and notOpposit(spots)):
    #         #place next to one of the enemy location
    #         print("place next to enemy")
    #         if((board[1][0] == enemiePos) or (board[0][1]) == enemiePos):
    #             return(0,0)
    #         else:
    #             return(2,2)
    #     print("random move in playable moves", spots)
    #     return (choice(spots)) #random move in playable moves

    # else: #player/not CPU
    #     x = int(input("X: "))
    #     y = int(input("Y: "))
    # return (x,y)        
#[0,0,0]
#[0,1,-1]
#[0,-1,0]

#[0,0,-1]
#[-1,1,1]
#[1,-1,-1]

#When CPU starts first:
#1st: random corner
#2nd: opposit corner

#1 random corner,2 center, 3 opposit corner, 4 defending loop
#1 random corner, not center, random corner that isn't opposit corner, defends or looses, wins or random corner
#
# 
#  

#1,2,3 : random corner



#When CPU plays second
#1st: if center taken : random corner, else : always center
#4th : if no corner taken and isOppositExisting = false: search for row/line with a -1 and put a 1 in it
#6th: take a corner

#unsupported : cpu:coin, p2:coin opposé, cpu: random corner, p2:between corners, cpu:?

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

def playTurn(board, pTurn, player,turn):
    spot = chooseSpot(player, board, pTurn, turn)

    while (not isSpotFree(spot,board)): #if spot not free, we ask the player to pick a new one
        print("Spot is taken already, please choose another spot.",board)
        spot = chooseSpot(player, board, pTurn,turn)
    updateSpot(spot, board, pTurn)

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
    
    print(players[pTurn] + " starts the game.")

    while (not isOver):
        playTurn(board, pTurn, players[pTurn],turn)

        isOver = isWinner(board)
        if(len(getPlayableSpots(board)) == 0):
            isOver = 1
        pTurn = pTurnSwitch(pTurn)

        consoleDisplay(board)
        turn +=1

    winner = pTurnSwitch(pTurn)
    if(isOver != 1):
        print(players[winner] + " won the game !")
    else:
        print("Draw, nobody won !")

playGame()