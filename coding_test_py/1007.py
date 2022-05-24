'''
백준 1007 벡터 매칭
'''
from itertools import combinations
import sys

def solve():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    total_x = 0 
    total_y = 0
    for x, y in P:
        total_x += x
        total_y += y
    combi = combinations(P, N//2)
    ans = sys.maxsize
    for temp in combi:
        sum_v = [0, 0]
        for x, y in temp:
            sum_v[0] += 2 * x
            sum_v[1] += 2 * y
        leng = ((total_x-sum_v[0])**2 + (total_y-sum_v[1])**2) ** 0.5
        ans = min(ans, leng)
    print(ans)

T = int(input())

for _ in range(T):
    solve()