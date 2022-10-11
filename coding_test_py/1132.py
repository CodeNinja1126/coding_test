'''
백준 1132번 합
'''
from collections import defaultdict
N = int(input())
weight = defaultdict(lambda:0)
flg = False
cant_zero = set()
for _ in range(N):
    nums = input()[::-1]
    for i,ch in enumerate(nums):
        weight[ch] += 10**i
    cant_zero.add(nums[-1])

tmp = 10000000000000
tmp_ch = 0
for k in weight.keys():
    if k in cant_zero:
        continue
    if tmp > weight[k]:
        tmp_ch = k
        tmp = weight[k]

if tmp_ch and len(weight.keys()) == 10:
    del weight[tmp_ch]

ans = 0
vals = sorted(list(weight.values()), reverse=True)
for i, val in enumerate(vals):
    ans += val * (9-i)

print(ans)