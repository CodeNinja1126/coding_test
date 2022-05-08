'''
백준 16947번 서울 지하철 2호선
그래프
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)


def search_ring(now_pos):
    path.append(now_pos)
    for d in graph[now_pos]:
        if len(path) > 1 and  d == path[-2]:
            continue
        elif d in path:
            for i, node in enumerate(path):
                if node == d:
                    for val in path[i:]:
                        is_ring[val] = 1
                    break
            return True
        else:
            if search_ring(d):
                return True
            path.pop()

def cal_dis(pos):
    q = [[0, [pos]]]
    while True:
        depth, in_path = q.pop(0)
        now_pos = in_path[-1]
        if is_ring[now_pos]:
            return depth
        for i in graph[now_pos]:
            if len(in_path) > 1 and  i == in_path[-2]:
                continue
            q.append([depth+1, in_path+[i]])


n = int(input())
graph = defaultdict(lambda:[])
for _ in range(n):
    s, d = map(int, input().split())
    graph[s].append(d)
    graph[d].append(s)

path = []
is_ring = [0 for i in range(n+1)]
search_ring(1)
for i in range(1,n+1):
    print(cal_dis(i))
