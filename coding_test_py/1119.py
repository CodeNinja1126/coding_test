'''
백준 1119번 그래프
'''
from collections import defaultdict
N = int(input())
g = defaultdict(lambda:[])
if N == 1:
    print(0)
    exit()
    
for i in range(N):
    flg = False
    for j, ch in enumerate(input()):
        if ch == 'Y':
            flg = True
            g[i].append(j)
    if flg == False:
        print(-1)
        exit()

visited = [False for _ in range(N)]

def dfs_1(d):
    visited[d] = True
    for c in g[d]:
        if visited[c] == False:
            dfs_1(c)

def dfs_2(d):
    c_visited[d] = True
    for c in g[d]:
        if len(route) > 2 and route[0] == c:
            tmp = 0
            for i in route:
                tmp += 1 << i
            cy_set.add(tmp)
        elif c_visited[c] == False:
            route.append(c)
            dfs_2(c)
            route.pop()

cl_num = 0
cy_set = set()

for i in range(N):
    if visited[i] == False:
        dfs_1(i)
        cl_num += 1

    c_visited = [False for _ in range(N)]
    route = [i]
    dfs_2(i)


if cl_num - len(cy_set) < 2:
    print(cl_num-1)
else:
    print(-1)