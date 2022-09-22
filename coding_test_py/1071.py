'''
백준 1071번 소트
'''
from collections import Counter

input()
N = list(map(int, input().split()))
N_num = Counter(N)
N_keys = sorted(N_num.keys())
ans = [] 

for i, n in enumerate(N_keys):
    if N_num[n] == 0:
        continue
    if N_num[n+1]:
        if i+2 >= len(N_keys):
            ans += [n+1 for _ in range(N_num[n+1])]
            N_num[n+1] = 0
            ans += [n for _ in range(N_num[n])]
        else:
            ans += [n for _ in range(N_num[n])]
            tmp_num = N_keys[i+2]
            ans.append(tmp_num)
            N_num[tmp_num] -= 1
    else:
        ans += [n for _ in range(N_num[n])]

print(*ans)