'''
백준 19236번 청소년 상어
삼성
'''
from copy import deepcopy
dirs = ((-1,0), (-1,-1), (0,-1), (1,-1),
        (1,0), (1,1), (0,1), (-1,1))
board = []
for _ in range(4):
    inp = list(map(int, input().split()))
    temp = []
    for i in range(4):
        temp.append([inp[i*2],inp[i*2+1]-1])
    board.append(temp)


def fish_move():
    ret = deepcopy(board)
    for i in range(1, 17):
        for j in range(4):
            for k in range(4):
                if ret[j][k] == 0 or ret[j][k][0] != i:
                    continue
                for l in range(8):
                    dir_i = (ret[j][k][1] + l) % 8
                    new_x = j + dirs[dir_i][0]
                    new_y = k + dirs[dir_i][1]
                    if new_x >= 4 or new_x < 0 or\
                        new_y >= 4 or new_y < 0 or\
                        shark_pos == [new_x, new_y]:
                         continue
                    
                    ret[j][k], ret[new_x][new_y] = \
                        ret[new_x][new_y], ret[j][k]
                    ret[new_x][new_y][1] = dir_i
                    break

                else:
                    continue
                break

            else:
                continue
            break

    return ret


    

def dfs():
    global shark_pos, shark_dir, food, ans, board
    ans = max(ans, food)
    for i in range(1,4):
        new_x = shark_pos[0] + dirs[shark_dir][0]*i
        new_y = shark_pos[1] + dirs[shark_dir][1]*i
        if new_x >= 4 or new_x < 0 or\
            new_y >= 4 or new_y < 0 or\
            board[new_x][new_y] == 0:
            continue
        
        temp_board = deepcopy(board)
        temp_pos = deepcopy(shark_pos)
        temp_dir = shark_dir
        temp_food = food
        
        # shark_move
        shark_pos = [new_x, new_y]
        shark_dir = board[new_x][new_y][1]
        food += board[new_x][new_y][0]
        board[new_x][new_y] = 0

        board = fish_move()
        dfs()

        board = temp_board
        shark_pos = temp_pos
        shark_dir = temp_dir
        food = temp_food

ans = -1

shark_pos = [0,0]
shark_dir = board[0][0][1]
food = board[0][0][0]
board[0][0] = 0
board = fish_move()

dfs()
print(ans)