'''
백준 1082번 방 번호
'''
N = int(input())
price = list(map(int, input().split()))
M = int(input())

dp = [[] for _ in range(M+1)]

def l2n(l):
    ret = 0
    for i, n in enumerate(l):
        ret += n * (10**i)
    return ret

for i, p in enumerate(price[1:]):
    try:
        if l2n(dp[p]) < i+1:
            dp[p] = [i+1]
    except:
        continue

for i in range(1, M):
    if not dp[i]:
        continue

    for j, p in enumerate(price):
        temp = dp[i] + [j]
        temp.sort()
        try:
            if l2n(dp[i+p]) < l2n(temp):
                dp[i+p] = temp
        except:
            continue

print(max(l2n(l) for l in dp))