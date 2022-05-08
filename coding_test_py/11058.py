'''
백준 11058번 크리보드
DP
'''
N = int(input())

dp = [0 for _ in range(100)]
buffer = [0 for _ in range(100)]

dp[0] = 1
dp[1] = 2
dp[2] = 3
dp[3] = 4
dp[4] = 5
dp[5] = 6
buffer[4] = 2
buffer[5] = 3

for i in range(6, N):
    cand_1 = 2*dp[i-3]
    buffer[i] = dp[i-3]
    cand_2 = 4*buffer[i-2]
    cand_3 = 3*buffer[i-1]
    dp[i] = max(cand_1, cand_2, cand_3)

print(dp[N-1])
