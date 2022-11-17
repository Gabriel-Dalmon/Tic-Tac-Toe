from random import randrange

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

def getPlayableSpots(board):
    spots = []
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col] == 0:
                spots.append(row,col)
    return spots

def chooseSpot(player, board, pTurn, turn):

    if player == "CPU":
        conditions = [2*(1 + (pTurn * -2)),2*(1 + (pTurnSwitch(pTurn) * -2))] #conditions[victoire,defaite]
        for condition in conditions:
            line = linesSum(condition,board) #("row",1)
            if(line[0] == "row"):
                for i in range (0,3):
                    if(board[line[1]][i] == 0):
                        return (line[1],i)
            elif(line[0] == "col"):
                for i in range (0,3):
                    if(board[i][line[1]] == 0):
                        return (i,line[1])
            elif(line[0] == "diag"):
                for i in range (0,3):
                    if(line[1] == 0):
                        if(board[i][i] == 0):
                            return (i,i)
                    elif(line[1] == 2):
                        if(board[i][2-i] == 0):
                            return (i,2-i)
        if(turn == 1):
            #randomCorner()
            pass
        elif(turn == 3):
            #oppositCorner()
            pass
        elif(turn == 4 and noCornerTaken() and notOpposit()):
            #place next to one of the enemy location
            pass
        return #random move in playable moves
        
#[0,-1,0]
#[0,1,0]
#[0,-1,0]

#[0,0,-1]
#[-1,1,1]
#[1,-1,-1]

#When CPU starts first:
#1st: random corner
#2nd: opposit corner

#When CPU plays second
#1st: if center taken : random corner, else : always center
#4th : if no corner taken and isOppositExisting = false: search for row/line with a -1 and put a 1 in it
#6th: take a corner

    else:
        x = int(input("X: "))
        y = int(input("Y: "))
    return (x,y)

def updateSpot(coords, board, pTurn):
    board[coords[1]][coords[0]] = 1 + (pTurn * -2) #if opposer = 0 then case = 1 | if opposer = 1 then case = -1

def isSpotFree(coords,board): #checks if the spot is free to be taken by a player
    if(board[coords[1]][coords[0]] == 0):
        return True

def isWinner(board): #if Win Condition is verified, then return win type and index of row, col or diag.
    winCond = [3,-3] #the winCond is verified if the sum of a row, col, diag is equal to 3 or -3.
    lDiagSum = board[0][0] + board[1][1] + board[2][2] #Diagonal starting top left
    rDiagSum = board[0][2] + board[1][1] + board[2][0] #Diagonal starting top right
    if(lDiagSum in winCond):
        return ("diag",0)
    elif(rDiagSum in winCond):
        return ("diag",1)
    else:
        for i in range(0,3):
            rowSum = sum(board[i])
            colSum = board[0][i] + board[1][i] + board[2][i]
            if (rowSum in winCond):
                return ("row",i)
            elif(colSum in winCond):
                return ("col",i)
    return None

def pTurnSwitch(pTurn):
    pTurn = 1 * (1 - pTurn) # if pTurn = 1 => then pTurn = 1*(1-1) = 0, if pTurn = 0 => then pTurn = 1*(1-0) = 1*1 = 1 || switches between 0 and 1
    return pTurn

def playTurn(board, pTurn, player,turn):
    spot = chooseSpot(player, board, pTurn, turn)

    while (not isSpotFree(spot,board)): #if spot not free, we ask the player to pick a new one
        print("Spot is taken already, please choose another spot.")
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
        pTurn = pTurnSwitch(pTurn)

        consoleDisplay(board)
        turn +=1

    winner = pTurnSwitch(pTurn)
    print(players[winner] + " won the game.")

playGame()