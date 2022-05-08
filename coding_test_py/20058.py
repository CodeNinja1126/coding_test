'''
백준 20058번 마법사 상어와 파이어스톰
삼성 sw 문제
'''
import sys
sys.setrecursionlimit(2**12)

dirs = ((0,1),(0,-1),(1,0),(-1,0))

def tornado(l):
    size = 2 ** l
    for i in range(0,board_size,size):
        for j in range(0,board_size,size):
            rotate(i,j,size)

def rotate(ii, jj, size):
    temp_board = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j, val in enumerate(board[ii+i][jj:jj+size]):
            temp_board[j][-1-i] = val

    for i_1, i_2 in enumerate(range(ii, ii+size)):
        for j_1, j_2 in enumerate(range(jj, jj+size)):
            board[i_2][j_2] = temp_board[i_1][j_1]
    del temp_board

def fire():
    temp_board = []
    for i in range(board_size):
        for j in range(board_size):
            close_ice = 0
            for k in range(4):
                new_i = dirs[k][0] + i
                new_j = dirs[k][1] + j
                if new_i < 0 or new_i >= board_size or\
                   new_j < 0 or new_j >= board_size:
                    continue
                if board[new_i][new_j] != 0:
                    close_ice +=1
            if close_ice < 3:
                temp_board.append((i,j))

    for i, j in temp_board:
        if board[i][j] > 0:
            board[i][j] -= 1 

def recursion(i, j, back_track):
    ans = 1
    back_track[i][j] = 1
    for ii, jj in dirs:
        new_i = ii + i
        new_j = jj + j
        if new_i < 0 or new_i >= board_size or\
           new_j < 0 or new_j >= board_size or\
           board[new_i][new_j] == 0 or\
           back_track[new_i][new_j]:
            continue
        ans += recursion(new_i, new_j, back_track)
    return ans


def count_size():
    back_track = [[0 for _ in range(board_size)] for _ in range(board_size)]
    ans = 0
    for i in range(board_size):
        for j in range(board_size):
            if not back_track[i][j] and board[i][j]:
                ans = max(ans, recursion(i, j, back_track))
    if ans == 1:
        ans = 0
    return ans


N, Q = map(int, input().split())
board_size = 2**N
board = [list(map(int, input().split())) for _ in range(board_size)]
L = list(map(int, input().split()))

for l in L:
    tornado(l)
    fire()
print(sum([sum(li) for li in board]))
print(count_size())