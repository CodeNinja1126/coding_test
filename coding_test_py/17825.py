'''
백준 17825번 주사위 윷놀이
삼성
'''
board = [(0, 1), # 시작
         (2, 2), (4, 3),(6, 4),(8, 5),(10, 6, 20),
         (12, 7),(14, 8),(16, 9),(18, 10),(20, 11, 23),
         (22, 12),(24, 13),(26, 14),(28, 15),(30, 16, 25),
         (32, 17),(34, 18),(36, 19),(38, 31),
         (13, 21),(16, 22),(19, 28),
         (22, 24),(24, 28),
         (28, 26),(27, 27),(26, 28),
         (25, 29),(30, 30),(35, 31),(40, 32),
         (0, 0) # 끝
         ]

nums = list(map(int, input().split()))

ans = 0
score = 0
path = []
horses = [board[0], board[0], board[0], board[0]]

def move(cell, num):
    if len(cell) == 3:
        cell = board[cell[2]]
        num -= 1

    for _ in range(num):
        if cell[1] == 0:
            return cell
        else:
            cell = board[cell[1]]
    return cell


def dfs(depth):
    global score, ans
    if depth == 10:
        ans = max(ans, score)
    else:
        for i in range(4):
            if horses[i][1] == 0:
                continue

            temp_cell = move(horses[i], nums[depth])
            if temp_cell[1] != 0 and\
               any(horses[j] is temp_cell for j in range(4)):
                continue
            horses[i], temp_cell = temp_cell, horses[i]
            score += horses[i][0]
            dfs(depth+1)
            score -= horses[i][0]
            horses[i] = temp_cell

dfs(0)
print(ans)