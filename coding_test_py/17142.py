'''
백준 17142번 연구소 3
삼성
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

board = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)

virus = []
check_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i,j))
        if not board[i][j]:
            check_list.append((i,j))

if all(all(row)for row in board):
    print(0)
    exit()

dirs = ((0,1),(0,-1),(1,0),(-1,0))

virus_map = []

for x, y in virus:
    tmp = [[0]*N for _ in range(N)]
    tmp[x][y] = 1
    tmp_time = 1
    flg = True
    while flg:
        flg = False
        for i in range(N):
            for j in range(N):
                if tmp[i][j] != tmp_time:
                    continue
                for k in range(4):
                    new_i, new_j = i + dirs[k][0], j + dirs[k][1]
                    if new_i < 0 or new_i >= N or\
                       new_j < 0 or new_j >= N or\
                       board[new_i][new_j] == 1 or\
                       tmp[new_i][new_j]:
                        continue
                    
                    tmp[new_i][new_j] = tmp_time+1
                    flg = True
        tmp_time += 1
    
    virus_map.append(tmp)

ans = 10000
combi = []

def count_time():
    ret = 0
    for i, j in check_list:
        min_val = 10000
        for k in combi:
            if virus_map[k][i][j]:
                min_val = min(min_val, virus_map[k][i][j])
        if min_val == 10000 or \
           min_val-1 >= ans:
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
