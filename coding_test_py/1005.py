'''
백준 1005 ACM Craft
'''
from collections import defaultdict, deque
import sys
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    direction = defaultdict(lambda:[])
    required = defaultdict(lambda:set())
    for _ in range(K):
        a, b = map(int, input().split())
        direction[a].append(b)
        required[b].add(a)
    purpose = int(input())

    ans = 0
    queue = deque()
    visited = [False for i in range(N+1)]
    cost = [0 for i in range(N+1)]
    for i in range(N):
        if i+1 not in required:
            queue.append(i+1)
            cost[i+1] = D[i]
    
    while 1:
        building = queue.popleft()
        if building == purpose:
            ans = cost[building]
            break
        visited[building] = True
        for next in direction[building]:
            cost[next] = max(cost[next], cost[building] + D[next-1])
            for temp in required[next]:
                if not visited[temp]:
                    break
            else:
                queue.append(next)

    print('정답', ans)