'''
백준 14503번 로봇 청소기
삼성
'''
N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
dirs = ((-1,0), (0,1), (1,0), (0,-1))

def check():
    global ans, r, c, d
    if board[r][c] == 0:
        board[r][c] = -1
        ans += 1
    for i in range(1, 5):
        new_r = r + dirs[(d-i)%4][0]
        new_c = c + dirs[(d-i)%4][1]
        if board[new_r][new_c] == 0:
            r = new_r
            c = new_c
            d = (d-i)%4
            return True
    r -= dirs[d][0]
    c -= dirs[d][1]
    if board[r][c] != 1:
        return True
    return False

while check():
    pass

print(ans)