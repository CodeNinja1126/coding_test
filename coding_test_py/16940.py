'''
백준 16940번 BFS 스페셜 저지
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

i_1 = 0
i_2 = 1
b_set = set([1])
while True:
    temp_node = ans_list[i_1]
    temp_child = set(edge[temp_node])
    temp_child -= b_set
    b_set |= temp_child
    temp_ans = set(ans_list[i_2:i_2+len(temp_child)])
    if temp_ans != temp_child:
        print(0)
        break 
    i_2 += len(temp_child)
    i_1 += 1
    if i_2 == len(ans_list):
        print(1)
        break