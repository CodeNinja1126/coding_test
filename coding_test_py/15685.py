'''
백준 15685번 드래곤 커브
삼성
'''
N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]

dirs= ((0,1), (-1,0), (0,-1), (1,0))

def draw(i, x, y, d, g):
    stack = [(x,y), (x+dirs[d][0], y+dirs[d][1])]
    board[x][y] , board[x+dirs[d][0]][y+dirs[d][1]] = i, i
    for _ in range(g):
        b_x, b_y = stack[-1]
        for a, b in list(stack[-2::-1]):
            tmp_a = a - b_x
            tmp_b = b - b_y
            tmp_a, tmp_b = tmp_b, -tmp_a
            tmp_a += b_x
            tmp_b += b_y
            stack.append((tmp_a, tmp_b))

        for a, b in stack:
            board[a][b] = i

def check():
    ans = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and\
               board[i+1][j] and\
               board[i][j+1] and\
               board[i+1][j+1]:
                ans += 1
    return ans 

for i in range(1, N+1):
    x, y, d, g = map(int, input().split())
    draw(i, y, x, d, g)

print(check())
