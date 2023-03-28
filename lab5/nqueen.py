# N Queen Problem using backtracking
import numpy

global N
N = 8

def displayOutput(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " | ")
        print()

# checkSafe function checks if row and upper, lower diagonal are attack-free
# no check for column since each time placed in a new column
# row checking only for left side till the column being placed in since no queens on the right side
# explanation by chatGPT: 
'''
Now, when we place a queen in a row, we only need to check if it attacks the queens to its left (i.e., the queens that have already been placed on the board in previous rows). This is because we have not placed any queens to the right of the current queen yet, so there are no queens in the same row or to the right to attack it.
By checking only the left side, we can significantly reduce the number of comparisons we need to make to determine if a queen is being attacked or not. This helps to optimize the algorithm and make it more efficient.
'''

def checkSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), 
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # zip combines two iterators so for a diagonal row and col changes together 

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False
 
    return True

def utilityFunction(board, col):
     
    # base case: If all queens are placed
    # then return true
    if col >= N:
        return True
 
    # Consider this column and try placing
    # this queen in all rows one by one
    for i in range(N):
 
        if checkSafe(board, i, col):
             
            # Place this queen in board[i][col]
            board[i][col] = 1
 
            # recursion to place rest of the queens (place in the next column, that's why no check for column)
            if utilityFunction(board, col + 1) == True:
                return True
 
            # If placing queen in board[i][col] doesn't lead to a solution, 
            # then queen from board[i][col]

            board[i][col] = 0 # quivalent to dropping the branch from state space search 
 
    # if the queen can not be placed in any row in this column col then return false
    return False
 
# This function solves the N Queen problem using Backtracking. 
# It mainly uses utilityFunction() to solve the problem. It returns false if queens
# cannot be placed, otherwise return true and placement of queens in the form of 1s.

# Note: there may be more than one solutions, this function prints one of the feasible solutions.
def solveNQueen():

    board = numpy.zeros(shape=(8,8))
    
    if utilityFunction(board, 0) == False:
        print ("Solution does not exist")
        return False
 
    displayOutput(board)
    return True
 
# main
solveNQueen()
