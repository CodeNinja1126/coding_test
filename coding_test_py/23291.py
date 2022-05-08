'''
백준 23291번 어항 정리
삼성
'''
dir = [[0,1],[1,0]]
def rotate():
    min_val = min(hang[-1])
    for i in range(N):
        if min_val == hang[-1][i]: 
            hang[-1][i] += 1
    hang[-2][1] = hang[-1][0]
    hang[-1][0] = 0
    while True:
        s_i = 0
        e_i = 0
        h_i = 0
        for i in range(N):
            if hang[-1][i]:
                s_i = i
                break
        for i in range(s_i,N):
            if not hang[-2][i]:
                e_i = i
                break
        else:
            e_i = N
        for i in range(N):
            if not hang[N-i-1][s_i]:
                h_i = i
                break
        if h_i + e_i > N:
            break
        for i in range(s_i, e_i):
            for j in range(N):
                if not hang[N-j-1][i]:
                    break
                hang[-1-(e_i-i)][e_i+j] = hang[N-j-1][i]
                hang[N-j-1][i] = 0


def exchange():
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(2):
                try:
                    if not hang[i][j]:
                        continue
                    if not hang[i+dir[k][0]][j+dir[k][1]]:
                        continue
                    sub_val = abs(hang[i+dir[k][0]][j+dir[k][1]] - hang[i][j])
                    sub_val //= 5
                    if hang[i+dir[k][0]][j+dir[k][1]] < hang[i][j]:
                        temp[i+dir[k][0]][j+dir[k][1]] += sub_val
                        temp[i][j] -= sub_val
                    else:
                        temp[i+dir[k][0]][j+dir[k][1]] -= sub_val
                        temp[i][j] += sub_val
                except:
                    continue
    for i in range(N):
        for j in range(N):
            hang[i][j] += temp[i][j]


def flatten():
    temp_li = []
    for i in range(N):
        if hang[-1][i]:
            for k in range(N):
                if hang[-1-k][i]:
                    temp_li.append(hang[-1-k][i])
                    hang[-1-k][i] = 0
    hang[-1] = temp_li

def pile():
    for i in range(N//2):
        hang[-2][-1-i] = hang[-1][i]
        hang[-1][i] = 0
    
    for i in range(N//2, 3*N//4):
        hang[-3][-1-i+N//2] = hang[-2][i]
        hang[-2][i] = 0
        hang[-4][-1-i+N//2] = hang[-1][i]
        hang[-1][i] = 0



N, K = map(int, input().split())
input_arr = list(map(int, input().split()))
hang = [[0 for _ in range(N)] for _ in range(N-1)]
hang.append(input_arr)
ans = 0
while True:
    if max(hang[-1]) - min(hang[-1]) <= K:
        break
    ans += 1
    rotate()
    exchange()
    flatten()
    pile()
    exchange()
    flatten()

print(ans)