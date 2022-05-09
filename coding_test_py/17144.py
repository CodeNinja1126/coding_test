'''
백준 17144 미세먼지 안녕!
시뮬레이션과 구현
'''
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
purifier = []


for i in range(R):
    if board[i][0] < 0:
        purifier.append((i,0))

dir_i = (0, -1, 0, 1)
dir_j = (1, 0, -1, 0)

def diffusion():
    temp_board = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] <= 0:
                continue

            diffused = 0
            for k in range(4):
                temp_i = i + dir_i[k]
                temp_j = j + dir_j[k]

                if temp_i >= R or 0 > temp_i or\
                   temp_j >= C or 0 > temp_j or\
                   board[temp_i][temp_j] == -1:
                    continue
                
                temp_board[temp_i][temp_j] += board[i][j] // 5
                diffused += board[i][j] // 5
            
            temp_board[i][j] -= diffused
    
    for i in range(R):
        for j in range(C):
            board[i][j] += temp_board[i][j]


def purifying():
    i, j = purifier[0]
    temp = 0
    dir_idx = 0
    while 1:
        temp_i = i + dir_i[dir_idx]
        temp_j = j + dir_j[dir_idx]
        if temp_i >= R or 0 > temp_i or\
           temp_j >= C or 0 > temp_j:
            dir_idx += 1
            temp_i = i + dir_i[dir_idx]
            temp_j = j + dir_j[dir_idx]
        
        i, j = temp_i, temp_j
        if board[i][j] == -1:
            break

        temp_temp = board[i][j]
        board[i][j] = temp
        temp = temp_temp

    i, j = purifier[1]
    temp = 0
    dir_idx = 0
    while 1:
        temp_i = i + dir_i[dir_idx]
        temp_j = j + dir_j[dir_idx]
        if temp_i >= R or 0 > temp_i or\
           temp_j >= C or 0 > temp_j:
            dir_idx -= 1
            temp_i = i + dir_i[dir_idx]
            temp_j = j + dir_j[dir_idx]

        i, j = temp_i, temp_j
        if board[i][j] == -1:
            break

        temp_temp = board[i][j]
        board[i][j] = temp
        temp = temp_temp


for _ in range(T):
    diffusion()
    purifying()

ans = 0    
for i in range(R):
    for j in range(C):
        ans += board[i][j] if board[i][j] >= 0 else 0

print(ans)