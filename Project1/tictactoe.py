"""
Tic Tac Toe Player
"""
# Stephnaie Becerra
# Marco Andrade
# Brandon Evans
# Jack Loague

from cmath import inf, pi
import math
from turtle import pos

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Count the number of x's and o's to determine who plays next
    xCounter = 0
    oCounter = 0

    for rows in board:
        for col in rows:
            if col == X:
                xCounter += 1
            elif col == O:
                oCounter += 1

    # Empty board means that X plays first
    if xCounter == 0 and oCounter == 0:
        return X
    # If the board has more X's than O, than it is O's turn
    elif xCounter > oCounter:
        return O
    # If the board has more O's than X, than it is X's turn
    else:
        return X

def actions(board): # handles the actions the AI can do
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for row in range(3):        # iterate through row
        for col in range(3):    # iterate through each cell
            if not board[row][col]: # if the board is empty add 
                possibleActions.add((row, col))
    
    return possibleActions


def result(board, action): # handles the result of the game
    """
    Returns the board that results from making move (i, j) on the board.
    """
    updatedBoard = board
    # Get the next player move, than reverse it to get the current player
    currentPlayer = player(board)

    # Place the token on the board
    updatedBoard[action[0]][action[1]] = currentPlayer

    return updatedBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # This method will call Score to find out who won the game
    winnerScore = score(board)

    if winnerScore == 1: # 1 means that x wins
        return X
    elif winnerScore == -1: # -1 means that o wins
        return O
    else:
        return None # anything else, return nothing

def terminal(board): # handles when and how the game should end
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X: # if x has three in a row, then they are a winner
        return True
    elif winner(board) == O: # if O has three in a row, then they are a winner
        return True 
    else:
        plays = 0 # will hold the count for entries

        for arr in board: # loop through the board and count the amount of x and 0
            plays += arr.count(X)
            plays += arr.count(O)
        
        if plays == 9: # if the board is full, the game ends
            return True
        else: # if the board is not full, continue the game
            return False

def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    xCounter = 0
    oCounter = 0

    n = len(board)

    # Check the rows
    for i in range(n):
        for j in range(n):
            if(board[i][j] == 'O'):
                oCounter += 1
            elif board[i][j] == 'X':
                xCounter += 1

        if(oCounter == 3):
            return -1
        elif(xCounter == 3):
            return 1
        else:
           xCounter = 0
           oCounter = 0

    # Check the columns
    for i in range(n):
        for j in range(n):
            if(board[j][i] == 'O'):
                oCounter += 1
            elif board[j][i] == 'X':
                xCounter += 1

        if(oCounter == 3):
            return -1
        elif(xCounter == 3):
            return 1
        else:
           xCounter = 0
           oCounter = 0

    # Check diagonals
    for i in range(n):
        if(board[i][i] == 'O'):
            oCounter += 1
        elif board[i][i] == 'X':
            xCounter += 1

        if(oCounter == 3):
            return -1
        elif(xCounter == 3):
            return 1

    # No winner found
    return 0

def evaluateBoard(board, aiToken):
    """
    Returns a minimum or maximum value score based on the suggested play.
    """
    if(aiToken == X):
        humanToken = O
    else:
        humanToken = X

    # Checking for Rows for X or O victory.
    for row in range(3) :    
        if (board[row][0] == board[row][1] and board[row][1] == board[row][2]) :       
            if (board[row][0] == aiToken) :
                return 10
            elif (board[row][0] == humanToken) :
                return -10
 
    # Checking for Columns for X or O victory.
    for col in range(3) :
        if (board[0][col] == board[1][col] and board[1][col] == board[2][col]) :
            if (board[0][col] == aiToken) :
                return 10
            elif (board[0][col] == humanToken) :
                return -10
 
    # Checking for Diagonals for X or O victory.
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) :
        if (board[0][0] == aiToken) :
            return 10
        elif (board[0][0] == humanToken) :
            return -10
    if (board[0][2] == board[1][1] and board[1][1] == board[2][0]) :
        if (board[0][2] == aiToken) :
            return 10
        elif (board[0][2] == humanToken) :
            return -10
 
    # Else if none of them have won then return 0
    return 0

# Recursive function for the Minimax Algo
def miniMaxSubFunction(board, depth, isMaximum, aiToken):
    """
    Consider all permutations the game can go and return the value
    """
    score = evaluateBoard(board, aiToken)
    
    if(aiToken == X):
        humanToken = O
    else:
        humanToken = X

    # Check if max won
    if (score == 10):
        return score
    
    # Check if min won
    if (score == -10) :
        return score

    # Check for tie
    if(terminal(board) == True):
        return 0

    # If it is the max's turn
    if(isMaximum):
        best = -inf

        # Check every cell
        for i in range(3) :        
            for j in range(3) :
                # Check if cell is empty
                if (board[i][j]==None) :
                 
                    # Make the move
                    board[i][j] = aiToken
 
                    best = max( best, miniMaxSubFunction(board, depth + 1, not isMaximum, aiToken) )
 
                    # Undo the move
                    board[i][j] = None
        return best

    # If it is the min's turn
    else:
        best = inf

        # Check every cell
        for i in range(3) :        
            for j in range(3) :
              
                # Check if cell is empty
                if (board[i][j]==None) :
                 
                    # Make the move
                    board[i][j] = humanToken
 
                    best = min( best, miniMaxSubFunction(board, depth + 1, not isMaximum, aiToken) )
 
                    # Undo the move
                    board[i][j] = None
        return best

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestVal = -99
    optimalMove = (-99, -99)
    possibleActions = actions(board)
    
    if(player(board) == X):
        aiToken = X
    else:
        aiToken = O
    
    # Evaluate each empty cell and find the optimal move
    for action in possibleActions:
        i = action[0]
        j = action[1]

        # Check the move
        board[i][j] = aiToken

        valueOfMove = miniMaxSubFunction(board, 0, False, aiToken)

        # Undo the move done
        board[i][j] = None

        # Keep the better move
        if(valueOfMove > bestVal):
            optimalMove = (i, j)
            bestVal = valueOfMove

    return optimalMove

