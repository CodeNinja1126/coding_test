'''
백준 16234 인구 이동
시뮬레이션과 구현
'''
import sys
sys.setrecursionlimit(2000)

N, L, R = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]
union_list = []
flg = True
dir_i = (1, -1, 0, 0)
dir_j = (0, 0, 1, -1)
ans = 0
people_num = 0

def dfs(i, j):
    global people_num
    visited[i][j] = ans
    union_list.append((i, j))
    people_num += map[i][j]
    for d_i in range(4):
        temp_i = i + dir_i[d_i]
        temp_j = j + dir_j[d_i]
        if 0 <= temp_i < N and\
           0 <= temp_j < N and\
           visited[temp_i][temp_j] != ans and\
           L <= abs(map[i][j] - map[temp_i][temp_j]) <= R:
            dfs(temp_i, temp_j)
    

while 1:
    flg = True

    for i in range(N):
        for j in range(N):
            people_num = 0
            union_list = []
            if visited[i][j] == ans:
                flg = False
                continue
            dfs(i, j)

            people_num //= len(union_list)
            for k, l in union_list:
                map[k][l] = people_num

    if flg:
        break

    ans += 1

print(ans)