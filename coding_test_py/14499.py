'''
백준 14499번 주사위 굴리기
삼성
'''
N, M, x, y, k = map(int, input().split())
dice = [0,0,0,0,0,0]
board = [list(map(int, input().split())) for _ in range(N)]
dirs = ((0,1), (0,-1), (-1,0), (1,0))

def roll_dice(d):
    if d == 0:
        dice[3], dice[0], dice[2], dice[5] = dice[5], dice[3], dice[0], dice[2]
    elif d == 1:
        dice[3], dice[0], dice[2], dice[5] = dice[0], dice[2], dice[5], dice[3]
    elif d == 2:
        dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]
    else:
        dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]

for d in map(int, input().split()):
    d -= 1
    new_x = x + dirs[d][0]
    new_y = y + dirs[d][1]
    if new_x < 0 or new_x >= N or\
       new_y < 0 or new_y >= M:
        continue
    x = new_x
    y = new_y
    roll_dice(d)
    if board[new_x][new_y]:
        dice[5], board[new_x][new_y] = board[new_x][new_y], 0
    else:
        board[new_x][new_y] = dice[5]
    print(dice[0])