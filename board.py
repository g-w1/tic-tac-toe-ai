
import math


def check(board):
    for x in wins:
        ocount = 0
        xcount = 0
        for i in x:
            if board[i] == 'x':
                xcount +=1
            if board[i] == 'o':
                ocount+=1
            if xcount == 3:
                return 1
            if ocount == 3:
                return -1
        if '' not in board:
            return 0
        else:
            return 'keepgoing'
def add_move(board,turn,index):
    if board[index] == '':
        board[index] = board
        return board
    else:
        return "0"
def bestMove(board):
    bestmove = -100
    bestset = (1,'o')
    for i,space in enumerate(board):
        if space == '':
            board[i] == 'o'
            score = minimax(board,0,False)
            board[i] = ''
            if score>bestmove:
                bestmove = score
                bestset = (i,'o')
    return bestset
def minimax(board,depth,turnMax):
    if check(board)!= "keepgoing":
        return check(board)/depth
    if turnMax:
        best = -100
        for i,space in enumerate(board):
            if space == '':
                board[i] == 'o'
                score = minimax(board,depth+1,False)
                board[i] = ''
                best = max(score,best)
        return best
    else:
        best = math.inf
        for i,space in enumerate(board):
            if space == '':
                board[i] == 'x'
                score = minimax(board,depth+1,True)
                board[i] = ''
                best = min(score,best)
        return best
wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
BOARD = ['' for _ in range(9)]
turn = 'x'
print(bestMove(['x','o','',
                'x','x','o',
                '','x','o']))