'''
백준 1208번 부분수열의 합 2
브루트포스 기타
'''
from collections import defaultdict

N,S = map(int, input().split())
nums = list(map(int, input().split()))
ans = 0
sum_1 = defaultdict(int)
sum_1[0] = 1
for temp_n in nums[:N//2]:
    temp_li = list(sum_1.items())
    for k,v in temp_li:
        sum_1[temp_n+k] += v

sum_2 = defaultdict(int)
sum_2[0] = 1
for temp_n in nums[N//2:]:
    temp_li = list(sum_2.items())
    for k,v in temp_li:
        sum_2[temp_n+k] += v

for s_1 in sum_1.keys():
    ans += sum_2[S - s_1] * sum_1[s_1]

if S == 0:
    print(ans - 1)
else:
    print(ans)