'''
백준 18500번 미네랄 2
'''
import sys
sys.setrecursionlimit(10001)
from copy import deepcopy

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

dirs = ((0,1), (0,-1), (1,0), (-1,0))

def find_cluster(i, j, board, cluster):
    if board[i][j] == 'x':
        cluster.append((i, j))
        board[i][j] = '.'
        for dir_i in range(4):
            new_i, new_j = i + dirs[dir_i][0], j + dirs[dir_i][1]
            if new_i >= R or new_j >= C or\
               new_i < 0 or new_j < 0 or\
               board[new_i][new_j] == '.':
                continue
            
            find_cluster(new_i, new_j, board, cluster)
    
    return cluster

def drop(cluster, board):
    for i, j in cluster:
        board[i][j] = '.'
    ans = False

    while 1:
        tmp = []
        for i, j in cluster:
            new_i = i + 1
            if new_i < R and board[new_i][j] == '.':
                tmp.append((new_i, j))
            else:
                break
        else:
            cluster = tmp
            ans = True
            continue
        break
    
    for i, j in cluster:
        board[i][j] = 'x'

    return ans


def gravity():
    global board
    visited = deepcopy(board)
    for i in range(R):
        for j in range(C):
            cluster = find_cluster(i, j, visited, [])
            if cluster:
                tmp_board = deepcopy(board)
                if drop(cluster, tmp_board):
                    board = tmp_board
                    return

def throw(r):
    global dir_flg
    if dir_flg:
        for i in range(C-1,-1,-1):
            if board[-r][i] == 'x':
                board[-r][i] = '.'
                break
    else:
        for i in range(C):
            if board[-r][i] == 'x':
                board[-r][i] = '.'
                break
    
    dir_flg = not dir_flg


dir_flg = False
input()
th_list = list(map(int, input().split()))
for i in th_list:
    throw(i)
    gravity()

for row in board:
    print(''.join(row))