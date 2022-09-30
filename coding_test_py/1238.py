'''
백준 1238번 파티
그래프
'''
import sys
from collections import defaultdict

input = sys.stdin.readline
N, M, X = map(int, input().split())
X -= 1
path_1 = defaultdict(lambda:{})
path_2 = defaultdict(lambda:{})

def dfs(i, total, path, visited):
    for dest, local in path[i].items():
        local += total
        if local < visited[dest]:
            visited[dest] = local
            dfs(dest, local, path, visited)

for _ in range(M):
    a, b, t = map(int, input().split())
    path_1[a-1][b-1] = t
    path_2[b-1][a-1] = t

visited_1 = [10000000 for _ in range(N)]
visited_1[X] = 0
visited_2 = [10000000 for _ in range(N)]
visited_2[X] = 0
dfs(X, 0, path_1, visited_1)
dfs(X, 0, path_2, visited_2)
    
print(max( i+j for i, j in zip(visited_1, visited_2)))