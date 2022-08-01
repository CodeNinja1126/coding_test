'''
백준 21610번 마법사 상어와 비바라기
삼성
'''
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
clouds = [[0] * N for _ in range(N)]
clouds[N-1][0] = 1
clouds[N-1][1] = 1
clouds[N-2][0] = 1
clouds[N-2][1] = 1
dirs = ((0,-1), (-1,-1), (-1, 0), (-1,1), (0,1), 
        (1,1), (1,0), (1,-1))

for _ in range(M):
    d, s = map(int, input().split())
    d -= 1
    temp_clouds = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if clouds[x][y] == 1:
                new_x = x + N*50 + s*dirs[d][0]
                new_y = y + N*50 + s*dirs[d][1]
                new_x %= N
                new_y %= N
                temp_clouds[new_x][new_y] = 1
                board[new_x][new_y] += 1
    clouds = temp_clouds

    temp_board = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if clouds[x][y]:
                for i in (1, 3, 5, 7):
                    new_x = x + dirs[i][0]
                    new_y = y + dirs[i][1]
                    if new_x >= N or new_x < 0 or\
                    new_y >= N or new_y < 0 or\
                    board[new_x][new_y] == 0:
                        continue
                    temp_board[x][y] += 1
        
    for x in range(N):
        for y in range(N):
            board[x][y] += temp_board[x][y]
    
    temp_clouds = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y] >= 2 and\
               clouds[x][y] != 1:
                temp_clouds[x][y] = 1
                board[x][y] -= 2 
    
    clouds = temp_clouds

ans = sum(sum(board[i]) for i in range(N))
print(ans)
