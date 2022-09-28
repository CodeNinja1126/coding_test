'''
백준 1035번 조각 움직이기
그래프
'''
from itertools import permutations

board = [list(input()) for _ in range(5)]
dirs = ((0,1),(0,-1),(1,0),(-1,0))
dp = [[[] for _ in range(5)]for _ in range(5)]
a_num = 0
for i in range(5):
    for j in range(5):
        if board[i][j] == '*':
            a_num += 1
            for k in range(5):
                for l in range(5):
                    dp[k][l].append(abs(i-k)+abs(j-l))

path = []
ans = 100

def check():
    stack = [path[0]]
    visited = [path[0]]
    while stack:
        i, j = stack.pop()
        for d_i in range(4):
            new_i, new_j = i+dirs[d_i][0], j+dirs[d_i][1]
            if new_i < 0 or new_i > 4 or\
               new_j < 0 or new_j > 4:
                continue
            if (new_i, new_j) in path and\
               (new_i, new_j) not in visited:
                stack.append((new_i, new_j))
                visited.append((new_i, new_j))
    
    if len(visited) != a_num:
        return True
    else:
        return False


def dfs(d):
    global ans
    if len(path) == a_num:
        if check():
            return
        for permu in permutations(range(a_num)):
            tmp = sum(dp[ii][jj][idx] for (ii, jj), idx in zip(path, permu))
            ans = min(tmp,ans)

    elif d == 25:
        return
    else:
        i = d//5
        j = d%5
        path.append((i,j))
        dfs(d+1)
        path.pop()
        dfs(d+1)


dfs(0)

print(ans)