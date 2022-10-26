'''
백준 1106번 호텔
'''
from sys import maxsize
C, N = map(int, input().split())
ads = []
dp = [maxsize for _ in range(1100)]
for _ in range(N):
    a, b = map(int, input().split())
    dp[b] = min(dp[b], a)
    ads.append((a,b))

for i in range(C):
    if dp[i] == 0:
        continue
    for a, b in ads:
        dp[i+b] = min(dp[i+b], dp[i]+a)

print(min(dp[C:]))

