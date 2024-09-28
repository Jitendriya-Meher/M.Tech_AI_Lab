def saveQueen( chessBoard, row, col):
    n = len(chessBoard)

    # check horizontally
    i = row
    j = col
    while j>=0:
        if chessBoard[i][j] == 'Q':
            return False
        j = j-1
    
    # check upper diagonal
    i = row
    j = col
    while i>=0 and j>=0:
        if chessBoard[i][j] == 'Q':
            return False
        j = j-1
        i = i-1
    
    # check lower diagonal
    i = row
    j = col
    while i<n and j>=0:
        if chessBoard[i][j] == 'Q':
            return False
        j = j-1
        i = i+1

    return True

def placeQueens( chessBoard , col):
    n = len(chessBoard)

    if col >= n:
        print(chessBoard)
        return

    for row in range (n):
        if saveQueen( chessBoard, row,col):
            chessBoard[row][col] = 'Q'
            placeQueens(chessBoard, col + 1)
        chessBoard[row][col] = ' '

n = 4

chessBoard = []
for i in range (n):
    temp = []
    for j in range (n):
        temp.append(" ")
    chessBoard.append(temp)

print("chess board : ")
# print(chessBoard)

placeQueens( chessBoard , 0)
