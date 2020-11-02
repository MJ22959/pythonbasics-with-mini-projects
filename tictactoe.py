from termcolor import colored
import random

board = [' ' for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter
        
def spaceIsFree(pos):
    return board[pos] == ' '

def boarddesign(board):
    print(colored('   |   |   ', 'green'))
    print(colored(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3], 'green'))
    print(colored('   |   |   ', 'green'))
    print(colored("************",'green'))
    print(colored('   |   |   ', 'green'))
    print(colored(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6], 'green'))
    print(colored('   |   |   ', 'green'))
    print(colored("************",'green'))
    print(colored('   |   |   ', 'green'))
    print(colored(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9], 'green'))
    print(colored('   |   |   ', 'green'))

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def IsWinner(b,l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or 
    (b[1] == l and b[4] == l and b[7] == l) or 
    (b[2] == l and b[5] == l and b[8] == l) or 
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input(colored("Please select the position to enter X from 1 to 9",'yellow'))
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X',move)
                else:
                    print(colored("Sorry,This space is already occupied!!!", 'red'))
            else:
                print(colored("Sorry,Please type the valid position between 1 and 9",'red'))

        except:
            print(colored("Please type the position number",'red')) 

def computerMove():
    possibleMoves = [ x for x, letter in enumerate(board) if letter == ' ' and x != 0 ]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if IsWinner(boardcopy,let):
                move = i
                return move
    
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
    print(colored("**********************************",'blue'))
    print(colored("Welcome to the game TicTacToe 2020",'blue'))
    print(colored("**********************************",'blue'))
    boarddesign(board)
    try:
        while not(isBoardFull(board)):
            if not(IsWinner(board, 'O')):
                playerMove()
                boarddesign(board)
            else:
                print(colored("Sorry, You Loose !!!",'red'))
                break
        
            if not(IsWinner(board, 'X')):
                move = computerMove()
                if move == 0:
                    print(" ")
                else:
                    insertLetter('O',move)
                    print(colored(("Computer placed an O on position",move, ':'),'yellow'))
                    boarddesign(board)
            else:
                print(colored("Congrats, You Win !!!", 'blue'))
                break
    except:
        print(colored("Tie game",'yellow'))
        

while True:
    x= input(colored("Do you wanna play ? (y/n) ",'yellow'))
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print(colored("**************************",'blue'))
        main()
    else:
        break




    


