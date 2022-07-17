'''
백준 1103번 게임
'''
from collections import deque

M, N = map(int, input().split())

dp = [[[set(),0] for _ in range(N)] for _ in range(M)]
board = [input() for _ in range(M)]

ans = 0
q = deque()
q.append((0,0,0,0,0))

dirs = ((0,1), (0, -1), (1,0), (-1,0))

while q:
    x, y, ans, pre_x, pre_y = q.popleft()
    track = dp[pre_x][pre_y][0]

    if x < 0 or x >= M or\
       y < 0 or y >= N or\
       board[x][y] == 'H':
        continue
    
    ans += 1

    if (x,y) in track:
        ans = -1
        break

    if ans == dp[x][y][1]:
        continue
    
    dp[x][y][0] |= track
    dp[x][y][0].add((x,y))
    dp[x][y][1] = ans

    for i in range(4):
        new_x = x+dirs[i][0]*int(board[x][y])
        new_y = y+dirs[i][1]*int(board[x][y])
        q.append((new_x, new_y, ans, x, y))    

print(ans)