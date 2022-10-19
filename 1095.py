'''
백준 1095번 마법의 구슬
'''
from collections import defaultdict

def prime(n):
    if n < 2:
        return []
    visit = [True if i%2 else False for i in range(n+1)]
    visit[1], visit[2] = False, True
    m = int(n ** 0.5)
    for i in range(3, m+1):
        if visit[i] == False:
            continue
        for j in range(i+i,n+1,i):
            visit[j] = False
    ret = []
    for i in range(2, n+1):
        if visit[i]:
            ret.append(i)
    return ret

def soinsu(n):
    global prime_li
    ret = defaultdict(lambda:0)
    while n > 1:
        for p in prime_li:
            if n % p == 0:
                ret[p] += 1
                n //= p
                break
    
    return ret

def num_soinsu(n):
    global prime_li
    ret = {}
    for p in prime_li:
        tmp = p
        ret[p] = 0
        while tmp <= n:
            ret[p] += n // tmp
            tmp *= p
    return ret

S, F, M = map(int, input().split())
total = S + F

prime_li = prime(M)
total_soinsu = num_soinsu(total)
s_soinsu = num_soinsu(S)
f_soinsu = num_soinsu(F)
for k in total_soinsu.keys():
    total_soinsu[k] -= s_soinsu[k]
    total_soinsu[k] -= f_soinsu[k]

for i in range(M, 1, -1):
    soinsu_dict = soinsu(i)
    for k in soinsu_dict.keys():
        if soinsu_dict[k] > total_soinsu[k]:
            break
    else:
        print(i)
        break
else:
    print(1)