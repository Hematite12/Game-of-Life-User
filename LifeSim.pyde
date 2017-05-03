import random
from Functions import *

MODE = "USER" # RANDOM or USER or GENETIC
THREAD = "OFF" # ON or OFF
PEN = "DRAW" # DRAW or ERASER
FRAMERATE = 200

def setup():
    global b, b2, bCopy, bInert, bChanged
    bInert, bChanged = makeBoards()
    if MODE == "RANDOM":
        b, b2 = makeRandomBoards(bInert)
        bCopy = [row[:] for row in b]
    else:
        b, b2 = makeBoards()
        bCopy = makeEmptyBoard()
    size(DIM*CELLDIM+10, DIM*CELLDIM+10)
    background(0)
    frameRate(FRAMERATE)

def mousePressed():
    if MODE == "USER" and THREAD == "OFF":
        if mouseX>5 and mouseX<DIM*CELLDIM+5:
            if mouseY>5 and mouseY<DIM*CELLDIM+5:
                xPos = (mouseX-5) // CELLDIM
                yPos = (mouseY-5) // CELLDIM
                flipState(b, b2, bInert, xPos, yPos)

def mouseDragged():
    if MODE == "USER" and THREAD == "OFF":
        if mouseX>5 and mouseX<DIM*CELLDIM+5:
            if mouseY>5 and mouseY<DIM*CELLDIM+5:
                xPos = (mouseX-5) // CELLDIM
                yPos = (mouseY-5) // CELLDIM
                if PEN == "DRAW":
                    flipLife(b, b2, bInert, xPos, yPos)
                else:
                    flipDeath(b, b2, bInert, xPos, yPos)

def keyPressed():
    global THREAD, PEN, b, b2, bCopy
    if key == " ":
        print(bInert)
        if THREAD == "OFF":
            THREAD = "ON"
        else:
            THREAD = "OFF"
    elif key == "e":
        if PEN == "DRAW":
            PEN = "ERASER"
        else:
            PEN = "DRAW"
    elif key == "r":
        reset()
    elif key == "c":
        bCopy = [row[:] for row in b]
    elif key == "v":
        b, b2 = getCopies(bCopy)
        THREAD = "OFF"

def reset():
    global THREAD, b, b2, bInert, bChanged
    THREAD = "OFF"
    bInert, bChanged = makeBoards()
    if MODE == "RANDOM":
        b, b2 = makeRandomBoards(bInert)
    elif MODE == "USER":
        b, b2 = makeBoards()

def draw():
    showBoard(b)
    if THREAD == "ON":
        updateBoard(b, b2, bInert, bChanged)