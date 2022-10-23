'''
백준 1248번 guess
'''
N = int(input())
tmp = input()
s_mat = [[0 for _ in range(N)] for _ in range(N)]
idx = 0
for i in range(N):
    for j in range(i,N):
        s_mat[i][j] = tmp[idx]
        idx += 1

mat = [[0 for _ in range(N)] for _ in range(N)]
ret = []
for i in range(N):
    if s_mat[i][i] == '-':
        mat[i][i] = -1
    elif s_mat[i][i] == '+':
        mat[i][i] = 1
    else:
        mat[i][i] = 0
    ret.append(mat[i][i])

def check(d):
    if d == 0:
        return True
    else:
        for i in range(d):
            mat[i][d] = mat[i][d-1] + mat[d][d]
            if (s_mat[i][d] == '-' and mat[i][d] < 0) or\
               (s_mat[i][d] == '+' and mat[i][d] > 0) or\
               (s_mat[i][d] == '0' and mat[i][d] == 0 ):
                continue
            else:
                return False
    return True
    
def dfs(d):
    if d == N:
        return True
    elif mat[d][d] == 0:
        if check(d) and dfs(d+1):
            return True
    else:
        tmp = mat[d][d]
        for i in range(1,11):
            mat[d][d] = tmp*i
            if check(d) and dfs(d+1):
                return True
            mat[d][d] = tmp

    return False

dfs(0)
print(' '.join([str(mat[i][i]) for i in range(N)]))