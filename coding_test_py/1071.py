'''
백준 1071번 소트
'''
from collections import Counter

input()
N = list(map(int, input().split()))
N.sort()
ans = [] 

while N:
    if N[0] + 1 in N[1:]:
        for i in range(1, len(N)):
            if N[0] + 1 < N[i]:
                temp_end = N[i]
                del N[i]
                temp = N[0]
                while True:
                    if N[0] != temp:
                        break 
                    ans.append(N[0])
                    del N[0]
                ans.append(temp_end)
                break
        else:
            for i in range(1, len(N)):
                if N[0] + 1 == N[i]:
                    ans.append(N[i])
                    del N[i]
                    break
    else:
        temp = N[0]
        while True and N:
            if N[0] != temp:
                break 
            ans.append(N[0])
            del N[0]

print(' '.join(map(str, ans)))