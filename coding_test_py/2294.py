'''
백준 2294번 동전 2
DP
'''
import sys

N, K = map(int, input().split())

coin_list = [int(input()) for _ in range(N)]
dp = [sys.maxsize for _ in range(K+1)]
dp[0] = 0

for i in range(K+1):
    for j in coin_list:
        try:
            dp[i+j] = min(dp[i+j], dp[i]+1)
        except:
            continue

if dp[K] == sys.maxsize:
    print(-1)
else:
    print(dp[K])
