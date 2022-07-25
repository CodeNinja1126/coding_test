'''
백준 21611번 마법사 상어와 블리자드
삼성
'''
dirs = ((-1, 0), (0, -1), (1, 0), (0, 1))
dir_tr = (0, 0, 2, 1, 3)

def b2l():
    now_x = (N+1)//2 - 1
    now_y = (N+1)//2 - 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[now_x][now_y] = 1
    now_dir = 0
    ret = []
    while now_x != 0 or now_y != 0:
        new_x = now_x + dirs[(now_dir+1)%4][0]
        new_y = now_y + dirs[(now_dir+1)%4][1]
        if visited[new_x][new_y]:
            now_x = now_x + dirs[now_dir][0]
            now_y = now_y + dirs[now_dir][1]
        else:
            now_x = new_x
            now_y = new_y
            now_dir = (now_dir+1)%4

        ret.append(board[now_x][now_y])
        visited[now_x][now_y] = 1
    return ret


def l2b(li):
    now_x = (N+1)//2 - 1
    now_y = (N+1)//2 - 1
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[now_x][now_y] = 1
    now_dir = 0
    i = 0
    while now_x != 0 or now_y != 0:
        new_x = now_x + dirs[(now_dir+1)%4][0]
        new_y = now_y + dirs[(now_dir+1)%4][1]
        if visited[new_x][new_y]:
            now_x = now_x + dirs[now_dir][0]
            now_y = now_y + dirs[now_dir][1]
        else:
            now_x = new_x
            now_y = new_y
            now_dir = (now_dir+1)%4
        board[now_x][now_y] = li[i]
        visited[now_x][now_y] = 1
        i += 1


def remove_zero(li):
    new_li = []
    for num in li:
        if num != 0:
            new_li.append(num)
    new_li += [0] * ((N**2-1) - len(new_li))
    return new_li


def magic(d, s):
    global ans
    d = dir_tr[d]
    now_x = (N+1)//2 - 1
    now_y = (N+1)//2 - 1
    for _ in range(s):
        now_x += dirs[d][0]
        now_y += dirs[d][1]
        board[now_x][now_y] = 0
    li = b2l()
    l2b(remove_zero(li))


def bomb():
    global ans
    flg = True
    while flg:
        flg = False
        li = b2l()
        pre_num = 0
        num_n = 0
        for i in range(len(li)):
            num = li[i]
            if pre_num != num:
                if num_n >= 4:
                    flg = True
                    ans += num_n * pre_num
                    li[i-num_n:i] = [0] * num_n
                pre_num = num
                num_n = 1
            else:
                num_n += 1

        l2b(remove_zero(li))


def change():
    li = b2l()
    pre_num = li[0]
    num_n = 1
    new_li = []
    for i in range(1, len(li)):
        num = li[i]
        if pre_num != num:
            new_li += [num_n, pre_num]
            pre_num = num
            num_n = 1
        else:
            num_n += 1
    
    l2b(remove_zero(new_li[:N**2-1]))


N, M = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for _ in range(M):
    d, s = map(int,input().split())
    magic(d,s)
    bomb()
    change()

print(ans)