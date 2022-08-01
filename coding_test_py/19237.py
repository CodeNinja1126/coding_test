'''
백준 19237번 어른 상어
'''
N, M, smell = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
smell_pos = [[[num, smell] if num > 0 else 0 for num in row] for row in board]
sharks = list(map(lambda x:int(x)-1, input().split()))
sharks.insert(0,0)
move_prior = [[list(map(lambda x:int(x)-1, input().split())) for _ in range(4)] for _ in range(M)]

dirs = ((-1,0),(1,0),(0,-1),(0,1))

ans = 0

while sum(sum(row) for row in board) != 1 and ans < 1000:
    # move
    for l in range(M):
        temp_shark = l+1
        temp_prior = move_prior[l][sharks[temp_shark]]
        for i in range(N):
            for j in range(N):
                if board[i][j] == temp_shark:
                    
                    for k in temp_prior:
                        new_i = i + dirs[k][0]
                        new_j = j + dirs[k][1]
                        if new_i >= N or new_i < 0 or\
                           new_j >= N or new_j < 0:
                            continue
                        if smell_pos[new_i][new_j] == 0:
                            board[i][j] = 0
                            if board[new_i][new_j] > temp_shark or\
                               board[new_i][new_j] == 0:
                                board[new_i][new_j] = temp_shark
                            sharks[temp_shark] = k
                            break
                    else:
                        # 자기 냄새
                        for k in temp_prior:
                            new_i = i + dirs[k][0]
                            new_j = j + dirs[k][1]
                            if new_i >= N or new_i < 0 or\
                               new_j >= N or new_j < 0:
                                continue
                            if smell_pos[new_i][new_j][0] == temp_shark:
                                board[i][j] = 0
                                if board[new_i][new_j] > temp_shark or\
                                   board[new_i][new_j] == 0:
                                    board[new_i][new_j] = temp_shark
                                sharks[temp_shark] = k
                                break
                    break
            else:
                continue
            break
    
    # smell
    for i in range(N):
        for j in range(N):
            if smell_pos[i][j]:
                smell_pos[i][j][1] -= 1
                if smell_pos[i][j][1] == 0:
                    smell_pos[i][j] = 0

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                smell_pos[i][j] = [board[i][j], smell]
    
    ans += 1

if ans == 1000:
    print(-1)
else:
    print(ans)