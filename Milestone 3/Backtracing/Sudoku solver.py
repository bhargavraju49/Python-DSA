def presentInRow(board,row,num):
    c=0
    for j in range(9):
        if board[row][j] == num:
            c+=1
            if c>1:
                return True
    return False

def presentInCol(board,col,num):
    c=0
    for j in range(9):
        if board[j][col] == num:
            c+=1
            if c>1:
                return True
    return False

def presentInBox(board,row,col,num):
    c=0
    for i in range(row,row+3):
        for j in range(col,col+3):
            if board[i][j] == num:
                c+=1
                if c>1:
                    return True
    return False

def isPossible(board,row,col,num):
    if(presentInRow(board,row,num)):
        return False
    if(presentInCol(board,col,num)):
        return False
    if(presentInBox(board,row-(row%3),col-(col%3),num)):
        return False
    return True


def solveSudoku (board):
    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                if isPossible(board,i,j,board[i][j]) is False:
                    return False
    return True

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')