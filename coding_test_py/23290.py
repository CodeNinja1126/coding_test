'''
백준 23291번 마법사 상어와 복제
삼성
'''
def fish_move():
    global fish_li
    temp_fish_li = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for fish in fish_li[i][j]:
                for dir_i in range(8):
                    new_dir_i = (fish-dir_i)%8
                    new_i = i + dir_fish[new_dir_i][0]
                    new_j = j + dir_fish[new_dir_i][1]
                    if new_i > 3 or new_i < 0 or \
                       new_j > 3 or new_j < 0:
                        continue
                    if shark_pos[0] == new_i and \
                       shark_pos[1] == new_j:
                        continue
                    if smell_board[new_i][new_j]:
                        continue
                    temp_fish_li[new_i][new_j].append(new_dir_i)
                    break
                else:
                    temp_fish_li[i][j].append(fish)
    fish_li,temp_fish_li = temp_fish_li,fish_li
    return temp_fish_li

def shark_move():
    best_score = -1
    move_list = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                temp_list = (i,j,k)
                temp_score = 0
                temp_pos = [x for x in shark_pos]
                backtrack = [[1 for _ in range(4)] for _ in range(4)]
                for move in temp_list:
                    temp_pos[0] += dir_shark[move][0]
                    temp_pos[1] += dir_shark[move][1]
                    if temp_pos[0] > 3 or temp_pos[0] < 0 or \
                       temp_pos[1] > 3 or temp_pos[1] < 0:
                        break
                    temp_score += len(fish_li[temp_pos[0]][temp_pos[1]]) * backtrack[temp_pos[0]][temp_pos[1]]
                    backtrack[temp_pos[0]][temp_pos[1]] = 0
                else:
                    if temp_score > best_score:
                        best_score = temp_score
                        move_list = temp_list

    for move in move_list:
        shark_pos[0] += dir_shark[move][0]
        shark_pos[1] += dir_shark[move][1]
        if len(fish_li[shark_pos[0]][shark_pos[1]]):
            fish_li[shark_pos[0]][shark_pos[1]] = []
            smell_board[shark_pos[0]][shark_pos[1]] = 3

def decrease_smell():
    for i in range(4):
        for j in range(4):
            if smell_board[i][j]:
                smell_board[i][j] -= 1

def copy_fish():
    for i in range(4):
        for j in range(4):
            fish_li[i][j] += original_fish_li[i][j]

dir_shark = [(-1,0), (0,-1), (1,0), (0,1)]
dir_fish = [(0, -1), (-1,-1), (-1,0), (-1, 1), (0,1), (1,1), (1,0), (1,-1)]

smell_board = [[0 for _ in range(4)] for _ in range(4)]
fish_li = [[[] for _ in range(4)] for _ in range(4)]

M, S = map(int, input().split())

for _ in range(M):
    f_x, f_y, d = map(int, input().split())
    fish_li[f_x-1][f_y-1].append(d-1)

shark_pos = list(map(int, input().split()))
shark_pos[0] -= 1
shark_pos[1] -= 1

for _ in range(S):
    original_fish_li = fish_move()
    shark_move()
    decrease_smell()
    copy_fish()

ans = 0

for i in range(4):
    for j in range(4):
        ans += len(fish_li[i][j])

print(ans)