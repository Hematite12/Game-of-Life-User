import random

DIM = 110
CELLDIM = 9
NUMSEEDS = 50
BOXDIM = 10
MARGIN = (DIM - BOXDIM) / 2

def makeNineActive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            board[i][j] = True

def makeNineInactive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            board[i][j] = False

def makeNeighborsActive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not i==0 or i==DIM-1 or j==0 or j==DIM-1:
                if not i==x and j==y:
                    board[i][j] = True

def makeNeighborsInactive(board, x, y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not i==0 or i==DIM-1 or j==0 or j==DIM-1:
                if not i==x and j==y:
                    board[i][j] = False

def makeBoards():
    board = [[False for i in range(DIM)] for j in range(DIM)]
    boardTwo = [[False for i in range(DIM)] for j in range(DIM)]
    return (board, boardTwo)

def makeEmptyBoard():
    return [[False for i in range(DIM)] for j in range(DIM)]

def makeFullBoard():
    return [[True for i in range(DIM)] for j in range(DIM)]

def makeRandomBoards(boardInerts):
    board = [[False for i in range(DIM)] for j in range(DIM)]
    boardTwo = [[False for i in range(DIM)] for j in range(DIM)]
    seeds = 0
    while seeds < NUMSEEDS:
        x = random.randrange(MARGIN, DIM-MARGIN)
        y = random.randrange(MARGIN, DIM-MARGIN)
        if not board[x][y]:
            board[x][y] = True
            boardTwo[x][y] = True
            makeNineActive(boardInerts, x, y)
            seeds += 1
    return (board, boardTwo)

def showBoard(board):
    for i in range(DIM):
        for j in range(DIM):
            cell = board[i][j]
            if cell:
                fill(0, 0, 255)
            else:
                fill(255)
            rect(i*CELLDIM+5,j*CELLDIM+5,CELLDIM,CELLDIM)

def sumNine(board, x, y):
    sum = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if board[i][j]:
                sum += 1
    return sum

def sumNeighbors(board, x, y):
    sum = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if not i==x and j==y:
                if board[i][j]:
                    sum += 1
    return sum

def updateInerts(boardInerts):
    for i in range(1, DIM-1):
        for j in range(1, DIM-1):
            boardInerts[i][j] = False

def updateBoard(board, boardTwo, boardInerts):
    changes = []
    for i in range(1, DIM-1):
        for j in range(1, DIM-1):
            if boardInerts[i][j]:
                num = sumNine(board, i, j)
                if board[i][j]:
                    if num<3 or num>4:
                        boardTwo[i][j] = False
                        changes.append([False, i, j])
                else:
                    if num==3:
                        boardTwo[i][j] = True
                        changes.append([True, i, j])
    updateInerts(boardInerts)
    for change in changes:
        board[change[1]][change[2]] = change[0]
        makeNineActive(boardInerts, change[1], change[2])

def getCopies(boardCopy):
    board = [row[:] for row in boardCopy]
    boardTwo = [row[:] for row in boardCopy]
    return (board, boardTwo)

def flipState(board, boardTwo, boardInerts, x, y):
    makeNineActive(boardInerts, x, y)
    if board[x][y]:
        board[x][y] = False
        boardTwo[x][y] = False
    else:
        board[x][y] = True
        boardTwo[x][y] = True

def flipLife(board, boardTwo, boardInerts, x, y):
    makeNineActive(boardInerts, x, y)
    board[x][y] = True
    boardTwo[x][y] = True

def flipDeath(board, boardTwo, boardInerts, x, y):
    makeNineActive(boardInerts, x, y)
    board[x][y] = False
    boardTwo[x][y] = False