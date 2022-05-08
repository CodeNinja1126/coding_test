'''
백준 10422번 괄호
DP
'''
T = int(input())
dp = [1,1,2]

def solve(N):
    global dp
    for i in range(len(dp)-1, N):
        dp.append(dp[i])
        for j in range(1,i+1):
            dp[i+1] += (dp[j-1] * dp[i+1-j])
            dp[i+1] %= 1000000007
    

for _ in range(T):
    N = int(input())
    if N % 2:
        print(0)
        continue

    N //= 2

    if N < len(dp):
        print(dp[N])
    else:
        solve(N)
        print(dp[N])