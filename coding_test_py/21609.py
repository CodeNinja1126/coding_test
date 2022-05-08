'''
백준 21609번 상어 중학교
삼성
'''
dirs = ((0,1),(0,-1),(1,0),(-1,0))
back_track = []
block_list = []

def search(ii, jj, color):
    global back_track
    global block_list
    block_list.append((ii,jj))
    if board[ii][jj] == color:
        back_track[ii][jj] = 1
    for i in range(4):
        new_i = ii + dirs[i][0]
        new_j = jj + dirs[i][1]
        if new_i >= 0 and new_i < N and\
           new_j >= 0 and new_j < N and\
           (board[new_i][new_j] == 0 or board[new_i][new_j] == color) and\
           (new_i, new_j) not in block_list:
            search(new_i, new_j, color)
            

def find_base(group):
    temp_board = [[0 for _ in range(N)] for _ in range(N)]
    for i, j in group:
        if board[i][j] > 0:
            temp_board[i][j] = 1
    
    for i in range(N):
        for j in range(N):
            if temp_board[i][j]:
                return (i, j)


def count_rainbow(group):
    ans = 0
    for i,j in group:
        if not board[i][j]:
            ans += 1
    return ans

def pop():
    global back_track
    global block_list
    group_list = []
    back_track = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and \
               not back_track[i][j]:
                block_list = []
                search(i, j, board[i][j])
                if len(block_list) > 1:
                    group_list.append(block_list)
    
    max_group = []
    for group in group_list:
        if len(group) < len(max_group):
            continue
        if len(group) > len(max_group):
            max_group = group
            continue
        if count_rainbow(group) < count_rainbow(max_group):
            continue
        if count_rainbow(group) > count_rainbow(max_group):
            max_group = group
            continue
        base_block = find_base(group)
        max_base_block = find_base(max_group)
        if base_block[0] < max_base_block[0]:
            continue
        if base_block[0] > max_base_block[0]:
            max_group = group
            continue
        if base_block[1] > max_base_block[1]:
            max_group = group
            continue
    
    for i,j in max_group:
        board[i][j] = -2
    
    global ans
    ans += len(max_group) ** 2

    return max_group


def gravity():
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if board[i][j] >= 0:
                k = 1
                while True:
                    if k+i >= N:
                        break
                    if board[i+k][j] == -2:
                        k +=1
                    else:
                        break
                temp = board[i][j]
                board[i][j] = -2
                board[i+k-1][j] = temp
                


def rotate():
    global board
    temp_board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j, val in enumerate(board[i][::-1]):
            temp_board[j][i] = val
    board = temp_board

N, M = map(int, input().split())
ans = 0
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

while pop():
    gravity()
    rotate()
    gravity()

print(ans)