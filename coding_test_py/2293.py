'''
백준 2293번 동전 1
DP
'''
N, K = map(int, input().split())
dp = [0 for _ in range(K+1)]
coins = []

for _ in range(N):
    coins.append(int(input()))

dp[0] = 1
for coin in coins:
    i = coin
    while True:
        if i > K: break
        dp[i] += dp[i-coin]
        i += 1

print(dp[K])
