'''
백준 1033 칵테일
'''

from collections import defaultdict

N = int(input())

def GCD(a, b):
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a

ans_li = [0 for _ in range(N)]
tree_dict = defaultdict(lambda:[])

def dfs(a, b, c):
    ans_li[a] *= c
    for k in tree_dict[a]:
        if k == b or ans_li[k] == 0:
            continue
        dfs(k, a, c)

for _ in range(N-1):
    a, b, p, q = map(int, input().split())
    tree_dict[a].append(b)
    tree_dict[b].append(a)

    new_p, new_q = 0, 0
    for i in range(1, 9):
        if p % i == 0 and q % i == 0:
            new_p = p // i
            new_q = q // i
    p, q = new_p, new_q

    if ans_li[a] == 0: ans_li[a] = 1
    if ans_li[b] == 0: ans_li[b] = 1
    a_val = ans_li[a]
    b_val = ans_li[b]
    g = GCD(a_val, b_val)
    a_rate = b_val // g * p
    b_rate = a_val // g * q
    g = GCD(a_rate, b_rate)
    a_rate = a_rate // g
    b_rate = b_rate // g

    dfs(a, b, a_rate)
    dfs(b, a, b_rate)

print(' '.join(map(str,ans_li)))