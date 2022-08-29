'''
백준 17143번 낚시왕
삼성
'''
import sys
input = sys.stdin.readline
R, C, M = map(int, input().split())
board = [[ 0 for _ in range(C)] for _ in range(R)]


def fishing(i):
    ret = 0
    for j in range(R):
        if board[j][i]:
            ret = board[j][i][-1]
            board[j][i] = 0
            break
    return ret

# new

moving_chart = []
moving_chart.append(list(range(R)) + list(range(R-2,0,-1)))
moving_chart.append(list(range(C)) + list(range(C-2,0,-1)))

for _ in range(M): 
    r,c,s,d,z = map(int, input().split())
    r -= 1
    c -= 1
    if d == 1 or d == 2:
        if d == 1:
            i = 2 * (R - 1) - r
        else:
            i = r
        d = 0
    else:
        if d == 4:
            i = 2 * (C - 1) - c
        else:
            i = c
        d = 1
    board[r][c] = (s,d,i,z)

def move():
    temp_board = [[ 0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                continue
            s = board[i][j][0]
            d = board[i][j][1]
            idx = board[i][j][2]
            z = board[i][j][3]

            temp_i = i
            temp_j = j
            if d == 0:
                idx = (idx + s) % len(moving_chart[d])
                temp_i = moving_chart[d][idx]
            else:
                idx = (idx + s) % len(moving_chart[d])
                temp_j = moving_chart[d][idx]
            
            if temp_board[temp_i][temp_j]:
                temp_board[temp_i][temp_j] = max((s,d,idx,z), temp_board[temp_i][temp_j], key=lambda x:x[-1])
            else:
                temp_board[temp_i][temp_j] = (s,d,idx,z)
    
    return temp_board

'''original
for _ in range(M): 
    r,c,s,d,z = map(int, input().split())
    board[r-1][c-1] = (s,d,z)

def move():
    temp_board = [[ 0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                continue
            s = board[i][j][0]
            d = board[i][j][1]
            z = board[i][j][2]
            temp_i = i
            temp_j = j
            if d == 1 or d == 2:
                if d == 1:
                    temp_i = 2 * (R - 1) - temp_i
                temp_i += s
                temp_i %= 2 * (R - 1)
                if temp_i >= R:
                    temp_i = (R-1) - (temp_i - (R-1))
                    d = 1
                else:
                    d = 2
            else:
                if d == 4:
                    temp_j = 2 * (C - 1) - temp_j
                temp_j += s
                temp_j %= 2 * (C - 1)
                if temp_j >= C:
                    temp_j = (C-1) - (temp_j - (C-1))
                    d = 4
                else:
                    d = 3
            
            if temp_board[temp_i][temp_j]:
                temp_board[temp_i][temp_j] = max((s, d, z), temp_board[temp_i][temp_j], key=lambda x:x[-1])
            else:
                temp_board[temp_i][temp_j] = (s,d,z)
    
    return temp_board

'''
ans = 0
for i in range(C):
    ans += fishing(i)
    board = move()

print(ans)
