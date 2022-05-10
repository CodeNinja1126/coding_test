'''
백준 20061번 모노미노도미노 2
시뮬레이션 구현
'''
green_board = [[False for _ in range(4)] for _ in range(6)]
blue_board = [[False for _ in range(6)] for _ in range(4)]

N = int(input())

ans_1 = 0
ans_2 = 0

def cal_ans_2():
    global ans_2
    for row in green_board:
        for val in row:
            if val:
                ans_2 += 1
    
    for row in blue_board:
        for val in row:
            if val:
                ans_2 += 1


def pop_green():
    global ans_1

    for i in range(2,6):
        if all(green_board[i]):
            del green_board[i]
            green_board.insert(0, [False, False, False, False])
            ans_1 += 1
            break
    
    for i in range(2):
        if any(green_board[i]):
            del green_board[-1]
            green_board.insert(0, [False, False, False, False])
            break


def pop_blue():
    global ans_1

    for i in range(2,6):
        if all(row[i] for row in blue_board):
            for row in blue_board:
                del row[i]
                row.insert(0, False)
            ans_1 += 1
            break

    for i in range(2):
        if any(row[i] for row in blue_board):
            for row in blue_board:
                del row[-1]
                row.insert(0, False)
            break    


def one_green(y):
    global green_board

    for i in range(6):
        if green_board[i][y]:
            green_board[i-1][y] = True
            break
    else:
        green_board[5][y] = True
    
    pop_green()
    

def one_blue(x):
    global blue_board

    for i in range(6):
        if blue_board[x][i]:
            blue_board[x][i-1] = True
            break
    else:
        blue_board[x][5] = True
    
    pop_blue()


def two_green(y):
    global green_board

    for i in range(6):
        if green_board[i][y] or green_board[i][y+1]:
            green_board[i-1][y] = True
            green_board[i-1][y+1] = True 
            break
    else:
        green_board[5][y] = True
        green_board[5][y+1] = True
    
    pop_green()


def two_blue(x):
    global blue_board

    for i in range(6):
        if blue_board[x][i] or blue_board[x+1][i]:
            blue_board[x][i-1] = True
            blue_board[x+1][i-1] = True
            break
    else:
        blue_board[x][5] = True
        blue_board[x+1][5] = True
    
    pop_blue()


for _ in range(N):
    T, X, Y = map(int, input().split())
    if T == 1:
        one_green(Y)
        one_blue(X)
    elif T == 2:
        two_green(Y)
        one_blue(X)
        one_blue(X)
    elif T == 3:
        one_green(Y)
        one_green(Y)
        two_blue(X)

print(ans_1)
cal_ans_2()
print(ans_2)