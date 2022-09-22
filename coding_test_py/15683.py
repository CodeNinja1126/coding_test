'''
백준 15683번 감시
삼성
'''
from copy import deepcopy
N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i,row in enumerate(room):
    for j,num in enumerate(row):
        if num and num < 6:
            cctv.append((i,j))

ans = N * M
dir_li = []
dirs = ((0, 1),(1,0), (0,-1),(-1,0))

def see(d, i, j, room):
    while 1:
        new_i = i + dirs[d][0]
        new_j = j + dirs[d][1]
        if new_i < 0 or new_i >= N or\
            new_j < 0 or new_j >= M or\
            room[new_i][new_j] == 6:
            break
        i, j = new_i, new_j
        if room[i][j]:
            continue
        room[i][j] = 7

def check(li):
    tmp_room = deepcopy(room)
    for (i, j), d in zip(cctv, li):
        if room[i][j] == 1:
            see(d, i, j, tmp_room)
        elif room[i][j] == 2:
            see(d, i, j, tmp_room)
            see(d+2, i, j, tmp_room)
        elif room[i][j] == 3:
            see(d, i, j, tmp_room)
            see((d+1)%4, i, j, tmp_room)
        elif room[i][j] == 4:
            see(d, i, j, tmp_room)
            see((d+1)%4, i, j, tmp_room)
            see((d+2)%4, i, j, tmp_room)
        else:
            see(d, i, j, tmp_room)
            see((d+1), i, j, tmp_room)
            see((d+2), i, j, tmp_room)
            see((d+3), i, j, tmp_room)
    ret = 0
    for row in tmp_room:
        for num in row:
            if num == 0:
                ret += 1
    
    return ret


def dfs(d):
    global ans
    if d == len(cctv):
        ans = min(ans, check(dir_li))
    else:
        if room[cctv[d][0]][cctv[d][1]] == 5:
            dir_li.append(0)
            dfs(d+1)
            dir_li.pop()
        elif room[cctv[d][0]][cctv[d][1]] == 2:
            for i in range(2):
                dir_li.append(i)
                dfs(d+1)
                dir_li.pop()
        else:
            for i in range(4):
                dir_li.append(i)
                dfs(d+1)
                dir_li.pop()

dfs(0)
print(ans)
