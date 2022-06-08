'''
백준 1053번 팰린드롬 공장
'''
import sys
st = input()

def swap(temp_st, i, j):
    return temp_st[:i] + temp_st[j] + temp_st[i+1:j] + temp_st[i] + temp_st[j+1:]

def rec(s, e):
    if s >= e:
        return 0

    if dp[s][e] < sys.maxsize:
        return dp[s][e]

    dp[s][e] = min(rec(s+1, e-1) + (st[s] != st[e]),
                   rec(s+1, e)+1, 
                   rec(s, e-1)+1)
                   
    return dp[s][e]

dp = [[sys.maxsize for _ in range(len(st))] for _ in range(len(st))]
ans = rec(0, len(st)-1)

for i in range(0, len(st)-1):
    for j in range(i+1, len(st)):
        st = swap(st, i, j)
        dp = [[sys.maxsize for _ in range(len(st))] for _ in range(len(st))]
        ans = min(ans, rec(0, len(st)-1)+1)
        st = swap(st, i, j)

print(ans)       