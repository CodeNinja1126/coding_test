'''
백준 11066번 파일 합치기
DP
'''
import sys

T = int(input())

for _ in range(T):
    K = int(input())
    P = list(map(int, input().split()))
    dp = [[0 for _ in range(K+1)] for _ in range(K+1)]

    for i in range(K-1):
        dp[i][i+2] = P[i] + P[i+1]
    
    for i in range(3, K+1):
        for j in range(K-i+1):
            score = sys.maxsize
            for k in range(j+1, j+i):
                score = min(dp[j][k] + dp[k][j+i], score)
            dp[j][j+i] = score + sum(P[j:j+i])

    print(dp[0][K])