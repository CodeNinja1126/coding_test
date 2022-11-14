'''
백준 1139번 울타리
'''
from collections import defaultdict
N = int(input())
bar = list(map(int, input().split()))
bar.sort()
bar_li = []
tmp = []
tri_dict = {}

def check():
    if tmp[0] + tmp[1] > tmp[2]:
        return True
    else:
        return False

def cal():
    p = sum(tmp)/2
    ret =(p*(p-tmp[0])*(p-tmp[1])*(p-tmp[2]))**0.5
    return ret

def dfs(d):
    global tmp
    if len(bar_li) == 3:
        tmp = [bar[bar_li[0]], bar[bar_li[1]], bar[bar_li[2]]]
        if check():
            val = 0
            for i in bar_li:
                val += 1 << i
            tri_dict[val] = cal()
    elif d == N:
        return
    else:
        dfs(d+1)
        bar_li.append(d)
        dfs(d+1)
        bar_li.pop()

dfs(0)

i = 0
ans = 0
comb_dict = tri_dict
while len(comb_dict) and i < 5:
    tmp_dict = defaultdict(lambda:0)
    for ck, cv in comb_dict.items():
        ans = max(ans, cv)
        for tk, tv in tri_dict.items():
            if tk & ck == 0:
                tmp_dict[tk | ck] = max(tmp_dict[tk | ck], cv + tv)
    comb_dict = tmp_dict
    i += 1

print(ans)