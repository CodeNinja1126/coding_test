'''
백준 16929번 육각 보드
그래프
'''
close_1 = [(0,0),(1,0),(0,1)]
close_2 = [(0,1),(1,0),(1,1)]
close = [(0,1),(1,0),(1,-1),(0,-1),(-1,0),(-1,1)]
color_num = 0

def inner_check(pos_i, pos_j, color):
    temp_set = set()
    for i in range(6):
        temp_i = pos_i + close[i][0]
        temp_j = pos_j + close[i][1]
        if temp_i < 0 or \
           temp_i >= N or \
           temp_j < 0 or \
           temp_j >= N:
           continue
        temp_set.add(block[temp_i][temp_j])
    if color in temp_set:
        return True
    else:
        return False


def check_block2(pos_i, pos_j, color):
    global color_num
    if inner_check(pos_i, pos_j, color+1):
        color_num = 3
        return True
    else:
        block[pos_i][pos_j] = color+1
        for i in range(6):
            temp_i = pos_i + close[i][0]
            temp_j = pos_j + close[i][1]
            if temp_i < 0 or \
               temp_i >= N or \
               temp_j < 0 or \
               temp_j >= N:
                continue
            if block[temp_i][temp_j] != 0:
                continue
            if check_block2(temp_i, temp_j, (color+1)%2):
                return True
    
    return False

def check_block(pos_i, pos_j):
    global color_num

    temp_close_num = 0
    for i in range(3):
        temp_i = pos_i + close_1[i][0]
        temp_j = pos_j + close_1[i][1]
        if block[temp_i][temp_j] == 0:
            temp_close_num += 1
    color_num = max(color_num, temp_close_num)
    
    temp_close_num = 0
    for i in range(3):
        temp_i = pos_i + close_2[i][0]
        temp_j = pos_j + close_2[i][1]
        if block[temp_i][temp_j] == 0:
            temp_close_num += 1
    color_num = max(color_num, temp_close_num)

N = int(input())
if N == 1:
    ch = input()
    if ch == '-': print(0)
    else: print(1)
else:
    block = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp_row = input()
        for j in range(N):
            if temp_row[j] == 'X':
                block[i][j] = 0

    for i in range(N-1):
        for j in range(N-1):
            check_block(i, j)
    
    if color_num == 2:
        for i in range(N):
            flg = 0
            for j in range(N):
                if block[i][j] != 0:
                    continue
                if check_block2(i, j, 0):
                    flg = 1
                    break
            if flg:
                break

    print(color_num)