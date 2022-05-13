'''
백준 17780 새로운 게임
시뮬레이션과 구현
'''
dir_i = (0, 1, 0, -1)
dir_j = (1, 0, -1, 0)
dir_tr = {1:0, 2:2, 3:3, 4:1}

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
piece= [[[] for _ in range(N)] for _ in range(N)]

for idx in range(K):
    i, j, dir = map(int, input().split())
    piece[i-1][j-1].append([idx, dir_tr[dir]])

def check():
    for i in range(N):
        for j in range(N):
            if len(piece[i][j]) >= 4:
                return False
    return True

def move():
    for i in range(K):
        flg = False
        temp = [0,0,0,0]
        for j in range(N):
            for k in range(N):
                for l, (idx, dir) in enumerate(piece[j][k]):
                    if idx == i:
                        flg = True
                        temp[2] = l
                        temp[3] = dir
                        break
                if flg:
                    temp[1] = k
                    break
            if flg:
                temp[0] = j
                break

        new_i = temp[0] + dir_i[temp[3]]
        new_j = temp[1] + dir_j[temp[3]]

        if new_i >= N or new_i < 0 or\
           new_j >= N or new_j < 0 or\
           board[new_i][new_j] == 2:
            new_i = temp[0] + dir_i[(temp[3]+2)%4]
            new_j = temp[1] + dir_j[(temp[3]+2)%4]
            piece[temp[0]][temp[1]][temp[2]][1] = (temp[3]+2)%4
            
            if new_i >= N or new_i < 0 or\
               new_j >= N or new_j < 0 or\
               board[new_i][new_j] == 2:
                pass
            elif board[new_i][new_j] == 0:
                piece[new_i][new_j] += piece[temp[0]][temp[1]][temp[2]:]
                piece[temp[0]][temp[1]] = piece[temp[0]][temp[1]][:temp[2]]
            elif board[new_i][new_j] == 1:
                piece[new_i][new_j] += piece[temp[0]][temp[1]][temp[2]:][::-1]
                piece[temp[0]][temp[1]] = piece[temp[0]][temp[1]][:temp[2]]

        elif board[new_i][new_j] == 0:
            piece[new_i][new_j] += piece[temp[0]][temp[1]][temp[2]:]
            piece[temp[0]][temp[1]] = piece[temp[0]][temp[1]][:temp[2]]
        elif board[new_i][new_j] == 1:
            piece[new_i][new_j] += piece[temp[0]][temp[1]][temp[2]:][::-1]
            piece[temp[0]][temp[1]] = piece[temp[0]][temp[1]][:temp[2]]

        if not check():
            return False

    return True


ans = 1
while move():
    ans += 1
    if ans > 1000:
        ans = -1
        break

print(ans)