import random

def table(board):
    # Function that prints out tic-tac-toe's table
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def playerChoice():
    # Asks the player which letter he chooses between X and O
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you choose X or O?')
        letter = input().upper()

    # The first element is the player's letter and the second is the computer's letter
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def firstPlayer():
    # Function that randomly chooses whether the computer or the player goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # Returns True if the player wants to play again, otherwise it returns False
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def winner(bo, le):
    # Returns Τrue if the player has won
    # "bo" stands for board and "le" stands for letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
    (bo[4] == le and bo[5] == le and bo[6] == le) or
    (bo[1] == le and bo[2] == le and bo[3] == le) or
    (bo[7] == le and bo[4] == le and bo[1] == le) or
    (bo[8] == le and bo[5] == le and bo[2] == le) or
    (bo[9] == le and bo[6] == le and bo[3] == le) or
    (bo[7] == le and bo[5] == le and bo[3] == le) or
    (bo[9] == le and bo[5] == le and bo[1] == le))

def tableCopy(board):
    # Duplicates the table list
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def freeSpace(board, move):
    # Checks if the chosen move is free
    return board[move] == ' '

def playerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freeSpace(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def randomMove(board, movesList):
    possibleMoves = []
    for i in movesList:
        if freeSpace(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def computerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Computer's moves using algorithm for A.I.

    # First, check if he can win in the next move
    for i in range(1, 10):
        copy = tableCopy(board)
        if freeSpace(copy, i):
            makeMove(copy, computerLetter, i)
            if winner(copy, computerLetter):
                return i

    # Check if the player could win on his next move, and block him
    for i in range(1, 10):
        copy = tableCopy(board)
        if freeSpace(copy, i):
            makeMove(copy, playerLetter, i)
            if winner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free
    move = randomMove(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free
    if freeSpace(board, 5):
        return 5

    # Move on one of the sides
    return randomMove(board, [2, 4, 6, 8])

def fullBoard(board):
    # Return True if all table spaces have been filled, otherwise return False
    for i in range(1, 10):
        if freeSpace(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    playerLetter, computerLetter = playerChoice()
    turn = firstPlayer()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Player's turn
            table(theBoard)
            move = playerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if winner(theBoard, playerLetter):
                table(theBoard)
                print('Congrats, you win!')
                gameIsPlaying = False
            else:
                if fullBoard(theBoard):
                    table(theBoard)
                    print('Tie!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn
            move = computerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if winner(theBoard, computerLetter):
                table(theBoard)
                print('You lose!')
                gameIsPlaying = False
            else:
                if fullBoard(theBoard):
                    table(theBoard)
                    print('Tie!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
