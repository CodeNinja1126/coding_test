'''
백준 16929번 Two Dots
그래프
'''
def search(pos_i, pos_j, depth):
    temp_ch = board[pos_i][pos_j]
    path[pos_i][pos_j] = depth
    for dir_i in range(4):
        temp_i = pos_i + dir[dir_i][0]
        temp_j = pos_j + dir[dir_i][1]
        if temp_i >= i or temp_i < 0 or \
           temp_j >= j or temp_j < 0:
            continue
        elif board[temp_i][temp_j] != temp_ch:
            continue
        elif depth == 1 and path[temp_i][temp_j] == 0:
            continue
        elif path[temp_i][temp_j] == 0:
            return True
        elif path[temp_i][temp_j] != -1:
            continue
        else: 
            if search(temp_i, temp_j, depth+1):
                return True
    path[pos_i][pos_j] = -1
    return False

i, j = map(int, input().split())
board = [input() for _ in range(i)]
path = [[-1 for _ in range(j)] for _ in range(i)]
dir = [[0,1], [1,0], [0,-1], [-1,0]]


for ii in range(i):
    flg = 0
    for ij in range(j):
        if search(ii, ij, 0):
            flg = 1
            break
    if flg:
        print('Yes')
        break
else:
    print('No')