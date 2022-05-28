'''
백준 1039 교환
'''
from itertools import combinations
ans = 0

def dfs(depth, i):
    global ans
    if depth == K:
        ans = max(ans, int(''.join(N)))

    elif i == len(N) - 2:
        if (K - depth) % 2:
            N[-1], N[-2] = N[-2], N[-1]
            ans = max(ans, int(''.join(N)))
            N[-1], N[-2] = N[-2], N[-1]
        else:
            ans = max(ans, int(''.join(N)))

    else:
        dfs(depth, i+1)
        for ii in range(i+1,len(N)):
            N[ii], N[i] = N[i], N[ii]
            if N[0] != '0':
                dfs(depth+1, i+1)
            N[ii], N[i] = N[i], N[ii]

N, K = map(int, input().split())
N = [ch for ch in str(N)]
if len(N) == 1 or\
   (len(N) == 2 and N[-1] == 0):
    print(-1)
else:
    dfs(0,0)
    print(ans)