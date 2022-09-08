from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

appeared = [0 for _ in range(N+1)]
roots = set()
graph = defaultdict(lambda:set())
for _ in range(M):
    a, b = map(int, input().split())
    appeared[b] += 1
    graph[a].add(b)

ans = []
for i in range(1, N+1):
    if not appeared[i]:
        ans.append(i)
        if graph[i]:
            roots.add(i)

while roots:
    tmp = set()
    for node in roots:
        for child in graph[node]:
            appeared[child] -= 1
            if not appeared[child]:
                ans.append(child)
                tmp.add(child)
    roots = tmp


print(' '.join(map(str, ans)))