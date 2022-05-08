'''
백준 11060번 점프 점프
DP
'''
N = int(input())
maze = list(map(int, input().split()))
dp = [10000 for _ in range(N)]

dp[0] = 0

for i, jump in enumerate(maze):
    for temp in range(i+1, i+jump+1):
        if temp >= N:
            break
        dp[temp] = min(dp[temp], dp[i]+1)


if dp[-1] == 10000:
    print(-1)
else:
    print(dp[-1])