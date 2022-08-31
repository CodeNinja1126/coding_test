'''
백준 2606번 바이러스
'''
from collections import defaultdict, deque

N = int(input())
M = int(input())

graph = defaultdict(lambda:[])
for a, b in (map(int, input().split()) for _ in range(M)):
    graph[a].append(b)
    graph[b].append(a)

virused = deque()
virused.append(1)
visited = [False] * 101

ans = 0

while virused:
    tmp = virused.popleft()
    if visited[tmp]:
        continue
    ans += 1  
    virused.extend(graph[tmp])
    visited[tmp] = True

print(ans-1)