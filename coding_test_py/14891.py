'''
백준 14891번 톱니바퀴
삼성
'''
from collections import deque

gears = []
for _ in range(4):
    gears.append(deque(map(int, input())))

def rotate(idx, d):
    if idx == 0:
        d_li = [1*d, -1*d, 1*d, -1*d]
        flg = 0
        for i in 1,2,3:
            if flg:
                d_li[i] = 0
            if gears[i-1][2] == gears[i][-2]:
                d_li[i] = 0
                flg = 1
    elif idx == 1:
        d_li = [-1*d, 1*d, -1*d, 1*d]
        if gears[1][-2] == gears[0][2]:
            d_li[0] = 0
        flg = 0
        for i in 2,3:
            if flg:
                d_li[i] = 0
            if gears[i-1][2] == gears[i][-2]:
                d_li[i] = 0
                flg = 1
    elif idx == 2:
        d_li = [1*d, -1*d, 1*d, -1*d]
        if gears[3][-2] == gears[2][2]:
            d_li[3] = 0
        flg = 0
        for i in 1,0:
            if flg:
                d_li[i] = 0
            if gears[i+1][-2] == gears[i][2]:
                d_li[i] = 0
                flg = 1
    else:
        d_li = [-1*d, 1*d, -1*d, 1*d]
        flg = 0
        for i in 2,1,0:
            if flg:
                d_li[i] = 0
            if gears[i+1][-2] == gears[i][2]:
                d_li[i] = 0
                flg = 1
    for i, d in enumerate(d_li):
        if d == 1:
            gears[i].appendleft(gears[i].pop())
        if d == -1:
            gears[i].append(gears[i].popleft())


for _ in range(int(input())):
    idx, d = map(int, input().split())
    rotate(idx-1, d)

ans = 0
for i in range(4):
    ans += gears[i][0] * (2 ** i)

print(ans)