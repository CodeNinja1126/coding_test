input()
N = list(map(int, input().split()))
dp = {}

for i in N:
    temp = 0
    for j in dp.keys():
        if i > j:
            temp = max(dp[j] + 1, temp)
    if temp == 0:
        dp[i] = 1
    else:
        dp[i] = temp
        

_, ans = max(dp.items(), key=lambda x: x[1])

print(ans)