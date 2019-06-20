# Modified version of sonar game from Invent your own computer games with python by Al Sweigart book
# View update log for significant changes

import random
import sys
pName = ''
difficulty = ''
xMax = 0
yMax = 0
diffTup = ()

def getHSpace(xMax):
    print("   " + ''.join(str(i%10) for i in range(xMax)))
    
def drawBoard(board, xMax, yMax):
    hline = ' '*4 # initial space at the top to account for the numbers on the left side
    for i in range(1, int((xMax+10)/10)):
        hline += (' ' * 9) + str(i)
        # print the numbers across the top
    print()
    print(hline)
    getHSpace(xMax)
    # print rows
    for i in range(yMax):
    # single-digit numbers need to be padded with an extra space
        if i < 10:
            extraSpace = ' '
        else:
            extraSpace = ''
        print('{0}{1} {2} {3}'.format(extraSpace, i, getRow(board, i), i))
    # print the numbers across the bottom
    getHSpace(xMax)
    print(hline)
    
def getRow(board, row):
    boardRow=''
    for i in range(xMax):
        boardRow+=board[i][row]
    return boardRow

def getNewBoard(xMax, yMax):
    board=[]
    for x in range(xMax):
        board.append([])
        for y in range(yMax):
            if random.randint(0,1)==0:
                board[x].append('\033[0;34m~\033[0m')
            else:
                board[x].append('\033[1;34m`\033[0m')
    return board
    
def getRandomChests(numChests):
    chests=[]
    for i in range(numChests):
        chests.append([random.randint(0,(xMax-1)), random.randint(0,(yMax-1))]) 
                                         #for placing the chests you must use one below the x & y max
    return chests
    
def isValidMove(x,y):
    return x >= 0 and x <= (xMax-1) and y >= 0 and y <= (yMax-1)
    
def makeMove(board, chests, x, y):
    if not isValidMove(x,y):
        return False
    smallestDistance = 100
    for cx, cy in chests:
        if abs(cx - x) > abs(cy - y):
            distance = abs(cx - x)
        else:
            distance = abs(cy - y)
        
        if distance < smallestDistance:
            smallestDistance = distance
    
    if smallestDistance <= 0:
        chests.remove([x, y])
        print(' You have found a sunken treasure chest at ({0}, {1})!'.format(x,y))
    else:
        if smallestDistance < 10:
            board[x][y] = str(smallestDistance)
            print(' Treasure detected at a distance of {0} from the sonar device.'.format(smallestDistance))
    
        else:
            board[x][y] = '0'
            print(' Sonar did not detect anything. All treasure chests out of range.')

def enterPlayerMove():
    print(' Where do you want to deploy the sonar device? (0-{0} 0-{1}) (or type quit)'.format((xMax-1),(yMax-1)))
    while True:
        move = input(' ')
        if 'q' in move.lower():
            print(' Thanks for playing!')
            sys.exit()
        
        move = move.split()
        if len(move)==2 and move[0].isdigit() and move[1].isdigit() and isValidMove(int(move[0]), int(move[1])):
            return [int(move[0]), int(move[1])]
        print(' Enter a number from 0 to {0}, a space, then a number from 0 to {1}. (or type quit)'.format((xMax-1),(yMax-1)))

def playAgain():
    playin=input(' Do you want to play again? yes or no ')
    if 'y' in playin:
        getDifficulty()
        Sonar()
    else:
        print(" Thanks for playing!")
        print()
        
def showInstructions():
    print('''  Instructions:
    You are the Captain of the Augustino, a treasure-hunting ship. Your current
    mission is to find the sunken treasure chests that are lurking in the part 
    of the ocean you are in to collect them.
    
    To play, enter coordinates (x y) of the point in the ocean you wish to drop a
    sonar device. The sonar can find out how far away the closest chest is to it.
    
    For example, the sonar device (the d) below marks where the device was dropped,
    and the 2's represent distances of 2 away from the device. The 4's represent
    distances of 4 away from the device.
    
       444444444
       4       4
       4 22222 4
       4 2   2 4
       4 2 \033[0;34md\033[0m 2 4
       4 2   2 4
       4 22222 4
       4       4
       444444444
       
    Press enter to continue...''')
    input(' ')
    print('''    For example, here is a chest (the c) located a distance of 2 away
    from the sonar device (the d):
        
        22222
        \033[1;33mc\033[0m   2
        2 \033[0;34md\033[0m 2
        2   2
        22222
    
    The point where the device was dropped will be marked with a 2.
    
    The Treasure chests don't move around. Sonar devices can detect treasure chests
    up to a distance of 9. If all chests are out of range, the point will be marked
    with a 0.
    
    If a device is directly dropped on a treasure chest, you have discovered
    the location of the chest, and it will be collected. The sonar device will
    remain there.
    
    When you collect a chest, all sonar devices will update to locate the next
    closest sunken treasure chest.
    
    There are 7 difficulty settings from beginner to custom. Each level changes the
    game a bit so try them all to see which one is your favorite.
    
    Press enter to continue...''')
    input(' ')
    print()
    
#start of screen display    
print(' \033[0;34mSONAR:\033[0m Treasures of the deep')
print()

def getPname():
    pName=input(' Please enter your name: ')
    print()
    print(' Welcome to SONAR Captain {0}, '.format(pName))
    return pName
getPname()                
                
viewInstruct = input(" Would you like to view the instructions before we begin? yes/no ")

if viewInstruct.lower().startswith('y'):
     showInstructions()
        
def getDifficulty():
    global difficulty
    difficulty=input('''
 What difficulty level would you like to play?
           
 1. \033[0;34mBeginner\033[0m 
 2. \033[0;32mIntermediate\033[0m 
 3. \033[1;33mAdvanced\033[0m 
 4. \033[0;33mExpert\033[0m 
 5. \033[0;31mNightmare\033[0m 
 6. \033[0;35mLucky Guess\033[0m
 7. \033[0;34mC\033[0;32mU\033[1;33mS\033[0;33mT\033[0;31mO\033[0;35mM\033[0m
           
 ''')
    return difficulty

def diffSettings():
    
    if difficulty =='1':
        sD = 16 #num of sonar devices
        tC = 2  #num of chests
        label= '\033[0;34mBeginner\033[0m' #blue 
        xMax=30 #board width
        yMax=15 #board height

    elif difficulty =='2':
        sD = 20
        tC = 4
        label='\033[0;32mIntermediate\033[0m' #green
        xMax=60
        yMax=15

    elif difficulty =='3':
        sD = 15
        tC = 5
        label='\033[1;33mAdvanced\033[0m' #yellow
        xMax=60
        yMax=15   

    elif difficulty =='4':
        sD = 60
        tC = 30
        label='\033[0;33mExpert\033[0m' #orange
        xMax=60
        yMax=15

    elif difficulty =='5':
        sD = 50
        tC = 25
        label='\033[0;31mNightmare\033[0m' #red
        xMax=60
        yMax=30

    elif difficulty == '6':
        sD = 1
        tC = 1
        label='\033[0;35mLucky Guess\033[0m' #purple
        xMax = 10
        yMax=5

    elif difficulty == '7':
        sD = int(input("Please enter the number of sonar devices: "))
        tC = int(input("Please enter the number of treasure chests: "))
        label = '\033[0;34mC\033[0;32mU\033[1;33mS\033[0;33mT\033[0;31mO\033[0;35mM\033[0m' #rainbow
        xMax = int(input("Please enter the width of the board: "))
        yMax = int(input("Please enter the height of the board: "))
                                                                                           
        print()    
        input(" You chose the {0} level of difficulty. Press enter to continue..." .format(label))
        print()
        print()
        
    global diffTup    
    diffTup = (sD, tC, label, xMax, yMax)
    return diffTup

def Sonar():

    global xMax
    global yMax
    getDifficulty()
    diffSettings()
    while True:
        
        #game setup
        sonarDevices = diffTup[0]
        theBoard = getNewBoard()
        theChests = getRandomChests(diffTup[1])
        drawBoard(theBoard)
        previousMoves = []
        
        while sonarDevices > 0:
            if sonarDevices > 1: 
                extraSsonar = 's'
                sword = 'are'
            else:
                extraSsonar = ''
                sword = 'is'
            
            if len(theChests) > 1:
                extraSchest = 's'
                cword = 'are'
                cword2 = 'were'
            else:
                extraSchest = ''
                cword = 'is'
                cword2 = 'was'
            
            #start of turn
            print(' There {0} {1} sonar device{2} ready to deploy. There {3} {4} treasure chest{5} to find.' .format(sword, sonarDevices, extraSsonar, cword, len(theChests), extraSchest))
            x, y = enterPlayerMove()
            previousMoves.append([x, y])
            
            moveResult = makeMove(theBoard, theChests, x, y)
            if not moveResult:
                continue
            else:
                if moveResult == 'You have found a sunken treasure chest at ({0}, {1})!'.format(x,y):
                    for x, y in previousMoves:
                        makeMove(theBoard, theChests, x, y)
                drawBoard(theBoard)
                print(moveResult)
            
            if theChests <= 0:
                print(' You have found all the sunken treasure chests! Congratulations and good game!')
                print(' You had {0} sonar device{1} left.'.format(sonarDevices, extraSsonar))
                break
            
            sonarDevices -= 1
            
            if sonarDevices <= 0:
                print(" We've run out of sonar devices! Now we have to turn the ship around and head")
                print(' for home with {0} treasure chest{1} still out there! Game Over.'.format(len(theChests), extraSchest))
                print()
                print()
                print(' The remaining chest{0} {1} at these coordinates: '.format(extraSchest, cword2))
                for x, y in theChests:
                    print(' {0}, {1}' .format(x, y))
        
        if not playAgain():
            sys.exit()       

if __name__=='__main__':
    Sonar()
