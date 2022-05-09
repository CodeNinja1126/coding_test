'''
백준 20057 마법사 상어와 토네이도
삼성
'''
dir_i = ((0,-1), (1,0), (0,1), (-1,0))
scatter_pos = (
    # 0
    ((-1, 1, 0.01), (1, 1, 0.01),
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, -1, 0.1), (1, -1, 0.1),
    (0, -2, 0.05), (0, -1, -1)),
    # 1
    ((-1, -1, 0.01), (-1, 1, 0.01),
    (0, -1, 0.07), (0, 1, 0.07),
    (0, -2, 0.02), (0, 2, 0.02),
    (1, -1, 0.1), (1, 1, 0.1),
    (2, 0, 0.05), (1, 0, -1)),
    # 2
    ((-1, -1, 0.01), (1, -1, 0.01),
    (-1, 0, 0.07), (1, 0, 0.07),
    (-2, 0, 0.02), (2, 0, 0.02),
    (-1, 1, 0.1), (1, 1, 0.1),
    (0, 2, 0.05), (0, 1, -1)),
    # 3
    ((1, -1, 0.01), (1, 1, 0.01),
    (0, -1, 0.07), (0, 1, 0.07),
    (0, -2, 0.02), (0, 2, 0.02),
    (-1, -1, 0.1), (-1, 1, 0.1),
    (-2, 0, 0.05), (-1, 0, -1))
)


def tornado():
    global dir
    visited[pos[0]][pos[1]] = True
    temp_dir = (dir + 1) % 4
    new_pos_i = pos[0] + dir_i[temp_dir][0]
    new_pos_j = pos[1] + dir_i[temp_dir][1]

    if visited[new_pos_i][new_pos_j]:
        pos[0] += dir_i[dir][0]
        pos[1] += dir_i[dir][1]
    else:
        dir = temp_dir
        pos[0] = new_pos_i
        pos[1] = new_pos_j

    scatter(dir, pos)
    return


def scatter(dir, pos):
    global ans
    total_sand = 0
    for i, j, k in scatter_pos[dir]:
        temp_i = pos[0] + i
        temp_j = pos[1] + j

        if k == -1:
            temp_sand = desert[pos[0]][pos[1]] - total_sand
        else:
            temp_sand = int(desert[pos[0]][pos[1]]*k)
            total_sand += temp_sand
        
        if temp_i >= 0 and temp_i < N and \
           temp_j >= 0 and temp_j < N:            
            desert[temp_i][temp_j] += temp_sand
        else:
            ans += temp_sand

    desert[pos[0]][pos[1]] = 0 
    return

N = int(input())
desert = [ list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

visited[N//2][N//2] = True
pos = [N//2, N//2-1]
dir = 0
ans = 0
scatter(dir, pos)

while pos[0] != 0 or pos[1] != 0:
    tornado()

print(ans)