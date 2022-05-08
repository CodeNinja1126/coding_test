'''
백준 16964번 DFS 스페셜 저지
그래프
'''
from collections import defaultdict

N = int(input())
edge = defaultdict(lambda:[])

for _ in range(N-1):
    s, d = map(int, input().split())
    edge[s].append(d)
    edge[d].append(s)

ans_list = list(map(int, input().split()))

i_1 = 1
visited = [False for _ in range(len(ans_list)+1)]
stack = [set([1])]

for num in ans_list:
    temp_set = stack.pop()
    visited[num] = True
    if num not in temp_set:
        print(0)
        break
    temp_set.remove(num)
    if len(temp_set):
        stack.append(temp_set)
    
    new_set = set()
    for node in edge[num]:
        if not visited[node]:
            new_set.add(node)
    
    if len(new_set):
        stack.append(new_set)

else:
    print(1)