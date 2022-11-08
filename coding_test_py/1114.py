'''
백준 1114번 통나무 자르기
이진 탐색
'''
L, K, C = map(int, input().split())
pos = list(set(map(int, input().split())))
pos.sort()
if K < C:
    C = K
bars = []
tmp = 0
for i in pos:
    bars.append(i - tmp)
    tmp = i
bars.append(L - tmp)

def cmp(l):
    tmp2 = 0
    c = 0
    a = 0
    for i, b in list(enumerate(bars))[::-1]:
        if b > l:
            return False
        if tmp2 + b <= l:
            tmp2 += b
        else:
            tmp2 = b
            c += 1
            a = pos[i]
                
    return c, a


def bin_search(a,b):
    if a >= b:
        return a
    mid = (a+b)//2
    tmp = cmp(mid)
    if tmp == False or tmp[0] > C:
        return bin_search(mid+1, b)
    else:
        return bin_search(a, mid)

ans = bin_search(1,L)
c, a = cmp(ans)
if c < C:
    a = pos[0]

print(ans, a)