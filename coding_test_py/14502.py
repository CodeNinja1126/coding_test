'''
백준 14502번 연구소
삼성
'''
from collections import deque
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

virus = []
for i in range(N):
    for j in range(M):
        if room[i][j] == 2:
            virus.append((i, j))

ans = 0
dirs = ((0,1), (0,-1), (1,0), (-1,0))

def check():
    global ans
    q = deque(virus)
    while q:
        i, j = q.popleft()
        for d_i in range(4):
            new_i, new_j = i+dirs[d_i][0], j+dirs[d_i][1]
            if new_i < 0 or new_i >= N or\
               new_j < 0 or new_j >= M or\
               room[new_i][new_j]:
                continue
            room[new_i][new_j] = 2
            q.append((new_i,new_j))
    
    tmp = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == 0:
                tmp += 1
            elif room[i][j] == 2:
                room[i][j] = 0
    
    for i, j in virus:
        room[i][j] = 2
    
    ans = max(ans, tmp)
    

def dfs(d, walls):
    if walls == 3:
        check()
    elif d == N*M:
        return
    else:
        i = d // M
        j = d % M
        if room[i][j] == 0:
            room[i][j] = 1
            dfs(d+1, walls+1)
            room[i][j] = 0
        dfs(d+1, walls)
        
dfs(0,0)
print(ans)