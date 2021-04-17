from sys import exit

b = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def player1():
    printboard()
    pos = int(input("Enter the number from 0-8 of where you would like to put your nought: "))
    global b
    if b[pos] != " ":
        print ("That space has already been used! Please choose somewhere else.")
        player1()
    b[pos] = "O"
    wincheck1()
            
def player2():
    global b
    printboard() 
    pos = int(input("Enter the number from 0-8 of where you would like to put your cross: "))
    if b[pos] != " ":
        print ("That space has already been used! Please choose somewhere else.")
        player2()
    b[pos] = "X"
    wincheck2()

def wincheck1():
    if "O" == b[0] == b[3] == b[6] or "O" == b[1] == b[4] == b[7] or "O" == b[2] == b[5] == b[8] or "O" == b[0] == b[1] == b[2] or "O" == b[3] == b[4] == b[5] \
    or "O" == b[6] == b[7] == b[8] or "O" == b[0] == b[4] == b[8] or "O" == b[6] == b[4] == b[2]:
        printboard()
        print ("Noughts is the winner!")
        playAgain()
    elif b.count(" ") == 0:
        print ("It's a draw!")
        playAgain()
    else:
        player2()

def wincheck2():
    if "X" == b[0] == b[3] == b[6] or "X" == b[1] == b[4] == b[7] or "X" == b[2] == b[5] == b[8] or "X" == b[0] == b[1] == b[2] or "X" == b[3] == b[4] == b[5] \
    or "X" == b[6] == b[7] == b[8] or "X" == b[0] == b[4] == b[8] or "X" == b[6] == b[4] == b[2]:
        printboard()
        print ("Crosses is the winner!")
        playAgain()
    elif b.count(" ") == 0:
        print ("It's a draw!")
        playAgain()
    else:
        player1()

def printboard():
    print ("              +---+---+---+ \n\
          0-2 | {0} | {1} | {2} | \n\
              +---+---+---+ \n\
          3-5 | {3} | {4} | {5} | \n\
              +---+---+---+ \n\
          6-8 | {6} | {7} | {8} | \n\
              +---+---+---+".format(b[0], b[1], b[2], b[3], b[4], b[5], b[6], b[7], b[8]))

def playAgain():
    again = input("Would you like to play again, Y/N? ")
    if again == "Y":
        global b
        b = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        player1()
    else:
        exit()

player1()