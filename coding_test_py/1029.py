'''
백준 1029 그림 교환
'''

from collections import defaultdict
import sys

N = int(input())
edges = defaultdict(lambda:{})
for i in range(N):
    for j, val in enumerate(input()):
        edges[i][j] = int(val)

ans = 0
dp = defaultdict(lambda:defaultdict(lambda:sys.maxsize))
def dfs(visited, last_v, last_price, depth):
    global ans
    ans = max(ans, depth)
    for v, pri in edges[last_v].items():
        new_visited = visited + 2**v
        if last_price > pri or\
           2**v & visited or\
           dp[v][new_visited] <= pri:
            continue
        dp[v][new_visited] = pri
        dfs(new_visited, v, pri, depth+1)

dfs(1, 0, 0, 0)

print(ans+1)
