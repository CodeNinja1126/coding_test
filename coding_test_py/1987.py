'''
백준 1987번 알파벳
'''
from collections import deque
R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - ord('A'), input())) for _ in range(R)]
path = 0
dirs = ((1,0), (0, -1), (-1,0), (0,1))

ans = 0

'''
def dfs(x, y, d):
    global ans, path
    ans = max(ans, d)

    for i in range(4):
        new_x, new_y = x+dirs[i][0], y+dirs[i][1]
        if new_x < 0 or new_x >= R or\
           new_y < 0 or new_y >= C or\
           path & 1 << board[new_x][new_y]:
            continue 
        
        path += 1 << board[new_x][new_y]
        dfs(new_x, new_y, d+1)
        path -= 1 << board[new_x][new_y]
'''

def bfs():
    global ans, path
    q = deque()
    q.append((0, 0, 1, path))
    visited = [[-1 for _ in range(C)] for _ in range(R)]
    while q:
        x, y, d, t_path = q.popleft()
        if x < 0 or x >= R or\
           y < 0 or y >= C or\
           t_path & 1 << board[x][y] or\
           t_path == visited[x][y]:
            continue
        
        ans = max(ans, d)
        visited[x][y] = t_path
        t_path += 1 << board[x][y]

        for i in range(4):
            new_x, new_y = x+dirs[i][0], y+dirs[i][1]
            q.append((new_x, new_y, d+1, t_path))

bfs()
print(ans)