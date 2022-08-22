'''
백준 11054번 가장 긴 바이토닉 부분 수열
DP
'''
N = int(input())
arr = list(map(int, input().split()))
dp = [[0, 0] for _ in range(N)]
for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i][0] = max(dp[j][0] + 1, dp[i][0])

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if arr[j] < arr[i]:
            dp[i][1] = max(dp[j][1] + 1, dp[i][1])

print(sum(max(dp, key=lambda x: sum(x)))+1)