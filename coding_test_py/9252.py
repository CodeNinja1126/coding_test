'''
백준 9252번 LCS 2
DP
'''
A = input()
B = input()

dp = ['' for _ in range(len(B))]
for ch1 in A:
    tmp1 = ''
    for i, ch2 in enumerate(B):
        tmp2 = dp[i]
        if ch2 == ch1:
            dp[i] = tmp1 + ch2
        tmp1 = max(tmp2, tmp1, key=lambda x:len(x))

ans = max(dp,key=lambda x:len(x))
print(len(ans))
print(ans)