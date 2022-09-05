'''
백준 16236번 아기 상어
삼성
'''
from collections import deque
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
shark_size = 2
ate = 0
ans = 0

dirs = ((-1,0), (0,-1), (0,1), (1,0))

def find_fish(shark_pos):
    visited = [[0]*N for _ in range(N)]
    q = deque()
    q.append((shark_pos[0], shark_pos[1], 0))
    visited[shark_pos[0]][shark_pos[1]] = 1
    candi = []
    flg = 0
    while q:
        x, y, z = q.popleft()
        if z > flg > 0:
            break

        if 0 < board[x][y] < shark_size:
            candi.append((x, y))
            flg = z

        if not flg:
            for i in range(4):
                new_x, new_y = x+dirs[i][0], y+dirs[i][1]
                if new_x < 0 or new_x >= N or\
                new_y < 0 or new_y >= N or\
                board[new_x][new_y] > shark_size or\
                visited[new_x][new_y]:
                    continue
                q.append((new_x, new_y, z+1))
                visited[new_x][new_y] = 1
    
    if flg:
        return *(min(candi, key=lambda x:(x[0],x[1]))), flg 
        
    return -1, -1, -1


def check():
    global ate, shark_size, ans
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                shark_pos = (i,j)
                break
        else:
            continue
        break

    i, j, k = find_fish(shark_pos)
    if i == -1:
        return False

    ate += 1
    ans += k
    if ate == shark_size and shark_size < 8:
        shark_size += 1
        ate = 0
    board[i][j] = 9
    board[shark_pos[0]][shark_pos[1]] = 0

    return True

while check():
    pass

print(ans)