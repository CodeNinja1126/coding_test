'''
백준 17142번 연구소 3
삼성
'''
import sys
from collections import deque
import time
input = sys.stdin.readline
N, M = map(int, input().split())

board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i,j))

if all(all(row)for row in board):
    print(0)
    exit()

dirs = ((0,1),(0,-1),(1,0),(-1,0))

start = time.time()
virus_map = []

for x, y in virus:
    tmp = [[0]*N for _ in range(N)]
    virus_q = deque()
    virus_q.append((x,y, 1))
    tmp[x][y] = 1
    while virus_q:
        i, j, tmp_time = virus_q.popleft()
        
        for k in range(4):
            new_i, new_j = i + dirs[k][0], j + dirs[k][1]
            if new_i < 0 or new_i >= N or\
                new_j < 0 or new_j >= N or\
                board[new_i][new_j] == 1 or\
                tmp[new_i][new_j]:
                continue
            virus_q.append((new_i, new_j, tmp_time+1))
            tmp[new_i][new_j] = tmp_time+1
    
    virus_map.append(tmp)

ans = 10000
combi = []

def count_time():
    ret = 0
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                continue
            min_val = 10000
            for k in combi:
                if virus_map[k][i][j]:
                    min_val = min(min_val, virus_map[k][i][j])
            if min_val == 10000:
                return 10000
            ret = max(ret, min_val)
    return ret - 1

def dfs(depth):
    global ans
    if len(combi) == M:
        ans = min(count_time(), ans)
    elif depth == len(virus):
        return
    else:
        dfs(depth+1)
        combi.append(depth)
        dfs(depth+1)
        combi.pop()

dfs(0)
if ans == 10000:
    print(-1)
else:
    print(ans)
