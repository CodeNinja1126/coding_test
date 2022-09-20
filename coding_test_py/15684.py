'''
백준 15684번 사다리 조작
삼성
'''
N, M, H = map(int, input().split())
ans = 0
ladder = [[0 for _ in range(N)] for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1
    ladder[a-1][b] = 2

def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if ladder[j][i] == 2:
                i -= 1
            elif ladder[j][i] == 1:
                i += 1

        if tmp != i:
            return False
    return True

line_num = 0

def dfs(d, idx):
    if line_num == d:
        if check():
            return True
    else:
        for ii in range(idx, (N-1)*H):
            i = ii // (N-1)
            j = ii % (N-1)
            if ladder[i][j+1] == 0 and\
                ladder[i][j] == 0:
                ladder[i][j] = 1
                ladder[i][j+1] = 2
                if dfs(d+1, ii):
                    return True
                ladder[i][j+1] = 0
                ladder[i][j] = 0
        return False

for i in range(4):
    line_num = i
    if dfs(0, 0):
        print(i)
        break
else:
    print(-1)
