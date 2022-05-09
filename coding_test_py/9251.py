'''
백준 9251 LCS
DP
'''
import re

str1 = input()
str2 = input()
N = len(str2)
dp = [0 for _ in range(N)]

for ch in str1:
    ch_i_li = list(re.finditer(rf'{ch}', str2))
    temp_dp = {}
    for match in ch_i_li:
        match_i = match.span()[0]
        if match_i == 0:
            temp_dp[match_i] = 1
            continue
        temp_dp[match_i] = dp[match_i-1] + 1
    
    for k, v in temp_dp.items():
        dp[k] = v

    temp = 0
    for i in range(N):
        temp = max(temp, dp[i])
        dp[i] = temp

print(dp[-1])