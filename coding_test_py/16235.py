'''
백준 16235번 나무 재테크
삼성
'''
import sys
input = sys.stdin.readline
from collections import deque
N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
board = [[5]* N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]
bunsik = [[0 for _ in range(N)] for _ in range(N)]

tmp = []
for _ in range(M):
    x, y, z = map(int, input().split())
    tmp.append((x-1, y-1, z))

tmp.sort(key=lambda x:x[-1])
for x, y, z in tmp:
    if len(trees[x][y]) and trees[x][y][-1][0] == z:
        trees[x][y][-1][1] += 1
    else:
        trees[x][y].append([z, 1])

dirs = ((-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def spring_summer():
    for i in range(N):
        for j in range(N):
            bunsik[i][j] = 0
            tmp_dq = deque()
            dead_trees = 0
            for z, num in trees[i][j]:
                if board[i][j] >= z * num:
                    board[i][j] -= z * num
                    tmp_dq.append([z+1, num])
                    if (z+1) % 5 == 0:
                        bunsik[i][j] += num
                elif board[i][j] // z:
                    edible = board[i][j] // z
                    board[i][j] %= z
                    tmp_dq.append([z+1, edible])
                    dead_trees += (z // 2) * (num - edible)
                    if (z+1) % 5 == 0:
                        bunsik[i][j] += edible
                else:
                    dead_trees += (z // 2) * num
            trees[i][j] = tmp_dq
            board[i][j] += dead_trees


def fall_winter():
    for i in range(N):
        for j in range(N):
            if bunsik[i][j]:
                for k in range(8):
                    new_i = i + dirs[k][0]
                    new_j = j + dirs[k][1]
                    if new_i < 0 or new_i >= N or\
                        new_j < 0 or new_j >= N:
                        continue
                    trees[new_i][new_j].appendleft([1, bunsik[i][j]])   
            board[i][j] += A[i][j]


for _ in range(K):
    spring_summer()
    fall_winter()

print(sum(sum(sum(a for _, a in dq) for dq in row) for row in trees))