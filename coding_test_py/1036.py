'''
백준 1036번 36진수
'''
from collections import defaultdict
N = int(input())
weight = defaultdict(lambda:0)
for _ in range(N):
    num = input()
    for i, ch in enumerate(num[::-1]):
        weight[ch] += 36 ** i

def func(x):
    ch, weight = x[0], x[1]
    if ord(ch) < ord('A'):
        num = int(ch)
    else:
        num = 10 + ord(ch) - ord('A')
    return weight*35 - weight*num

weight_li = sorted(list(weight.items()), key=func, reverse=True)
K = int(input())

for ch, val in weight_li[:K]:
    if ch == 'Z':
        continue
    weight['Z'] += weight[ch]
    del weight[ch]

ans = 0

for ch, val in weight.items():
    if ord(ch) < ord('A'):
        num = int(ch)
    else:
        num = 10 + ord(ch) - ord('A')

    ans += num * val

i = 1
ret = []
while ans != 0:
    ob = 36 ** i
    tmp = ans % ob
    ans -= tmp
    tmp //= 36 ** (i-1)
    
    if tmp < 10:
        tmp = str(tmp)
    else:
        tmp = chr(ord('A') + tmp - 10)

    ret.append(tmp)
    i += 1

ret.reverse()
if ret:
    print(''.join(ret))
else:
    print(0)
