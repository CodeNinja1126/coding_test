'''
백준 23291번 온풍기 안녕!
삼성
'''
from collections import defaultdict

dir_fpung = [
    (0,1),(0,-1),(-1,0),(1,0)
]
dir_pung = [
    ((0,1),(-1,1),(1,1)),
    ((0,-1),(-1,-1),(1,-1)),
    ((-1,0),(-1,1),(-1,-1)),
    ((1,0),(1,1),(1,-1))
]

def recursion(i, j, dir, therm, temp_board):
    if therm == 0 or \
       i >= R or i < 0 or \
       j >= C or j < 0 or \
       temp_board[i][j]:
        return
    else:
        temp_board[i][j] = therm
        ii, jj = dir_pung[dir][0]
        if (ii, jj) not in walls[(i,j)]:
            recursion(i+ii, j+jj, dir, therm-1, temp_board)
        for ii, jj in dir_pung[dir][1:]:
            if dir == 0 or dir == 1:
                if (ii, 0) in walls[(i,j)] or \
                   (0, jj) in walls[(i+ii,j)]:
                    continue
                recursion(i+ii, j+jj, dir, therm-1, temp_board)
            else:
                if (0, jj) in walls[(i,j)] or \
                   (ii, 0) in walls[(i,j+jj)]:
                    continue
                recursion(i+ii, j+jj, dir, therm-1, temp_board)

def pung():
    for i, j, dir in onpung:
        temp_board = [[0 for _ in range(C)] for _ in range(R)]
        recursion(i+dir_fpung[dir][0], j+dir_fpung[dir][1], dir, 5, temp_board)
        for ii in range(R):
            for jj in range(C):
                board[ii][jj] += temp_board[ii][jj]

def exchange():
    temp_board = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            for k in (0,3):
                if dir_fpung[k] in walls[(i,j)]:
                    continue
                new_i, new_j = i+dir_fpung[k][0], j+dir_fpung[k][1]
                if new_i >= R or new_i < 0 or \
                    new_j >= C or new_j < 0:
                    continue
                sub_therm = abs(board[i][j]-board[new_i][new_j])//4
                if board[i][j] > board[new_i][new_j]:
                    temp_board[i][j] += -sub_therm
                    temp_board[new_i][new_j] += sub_therm
                else:
                    temp_board[i][j] += sub_therm
                    temp_board[new_i][new_j] += -sub_therm

    for i in range(R):
        for j in range(C):
            board[i][j] += temp_board[i][j]

def decrease():
    for i in range(R):
        if board[i][0]:
            board[i][0] -= 1
        if board[i][-1]:
            board[i][-1] -= 1

    for i in range(1,C-1):
        if board[0][i]:
            board[0][i] -= 1
        if board[-1][i]:
            board[-1][i] -= 1

def check_th():
    for i, j in therm_can:
        if board[i][j] < K:
            return False
    else:
        return True

R, C, K = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
onpung = []
therm_can = []
walls = defaultdict(lambda:[])

for i in range(R):
    row = map(int, input().split())
    for j, num in enumerate(row):
        if num:
            if num == 5:
                therm_can.append((i,j))
            else:
                onpung.append((i,j,num-1))
            
num = int(input())
for _ in range(num):
    row = list(map(int, input().split()))
    if row[2]:
        walls[(row[0]-1, row[1]-1)].append(0)
        walls[(row[0]-1, row[1]-1+1)].append(1)
    else:
        walls[(row[0]-1, row[1]-1)].append(2)
        walls[(row[0]-1-1, row[1]-1)].append(3)

for i, j in walls.keys():
    temp_set = set()
    for dir in walls[(i,j)]:
        temp_set.add(dir_fpung[dir])
    walls[(i,j)] = temp_set

ans = 0
while True:
    pung()
    exchange()
    decrease()
    ans += 1
    if check_th() or ans == 101: break

print(ans)