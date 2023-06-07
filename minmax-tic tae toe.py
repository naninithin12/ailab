board=['_']*9
player='x'
ai='o'
def print_board(board):
    for i in range(0,9,3):
        print(*board[i:i+3])
def check(board,play):
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2]==play:
            return True
    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6]==play:
            return True
    if board[0]==board[4]==board[8]==play or board[6]==board[4]==board[2]==play:
        return True
    return False
def is_full(board):
    return '_' not in board
def minmax(board,depth,max_ai):
    if check(board,ai):
        return 1
    elif check(board,player):
        return -1
    elif is_full(board):
        return 0
    if max_ai:
        max_eval=float('-inf')
        for i in range(0,9):
            if board[i]=='_':
                board[i]=ai
                eval=minmax(board,depth+1,False)
                board[i]='_'
                max_eval=max(max_eval,eval)
        return max_eval
    else:
        mineval=float('inf')
        for i in range(0,9):
            if board[i]=='_':
                board[i]=player
                eval=minmax(board,depth+1,True)
                board[i]='_'
                mineval=min(mineval,eval)
        return mineval
def make_move(board):
    best=float('-inf')
    best_move=None
    for i in range(9):
        if board[i]=='_':
            board[i]=ai
            eval=minmax(board,0,False)
            board[i]='_'
            if eval > best:
                best=eval
                best_move=i
    board[best_move]=ai
def play():
    while not check(board,player) and not check(board,ai) and not is_full(board):
        print_board(board)
        print('player Turn')
        w=int(input('enter 0-8: '))
        if board[w] !='_':
            print('invalid')
            continue
        board[w]=player
        if check(board,player) or is_full(board):
            break
        print_board(board)
        print('ai turn')
        make_move(board)
        
    print_board(board)
    if check(board,player):
        print('you won')
    elif check(board,ai):
        print('ai won')
    else:
        print('tie match')
play()
    
        
        