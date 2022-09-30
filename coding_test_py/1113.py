'''
백준 1113번 수영장 만들기
그래프
'''
N, M = map(int, input().split())
pool = [list(map(int, input())) for _ in range(N)]

dirs = ((0,1), (0,-1), (1,0), (-1,0))
def dfs(i,j):
    global height
    l_h = pool[i][j]
    for d_i in range(4):
        new_i = i + dirs[d_i][0]
        new_j = j + dirs[d_i][1]
        if new_i < 0 or new_i >= N or\
           new_j < 0 or new_j >= M:
            return False
        if (new_i, new_j) in path:
            continue
        if pool[new_i][new_j] > l_h:
            height = min(height, pool[new_i][new_j])
            continue
        path.add((new_i, new_j))
        if dfs(new_i, new_j) == False:
            return False

    return True


ans = 0
for i in range(N):
    for j in range(M):
        path = set()
        path.add((i,j))
        height = 10
        if dfs(i, j):
            for k, l in path:
                if height > pool[k][l]:
                    ans += height - pool[k][l]
                    pool[k][l] = height

print(ans)
