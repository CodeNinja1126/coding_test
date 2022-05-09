'''
백준 20056 파이어볼
삼성
'''
dir_i = ((-1,0), (-1,1), (0,1), (1,1),
         (1,0), (1,-1), (0,-1), (-1,-1))

def move():
    global board
    temp_board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for m, s, d in board[i][j]:
                new_i = (i + dir_i[d][0]*s)%N
                new_j = (j + dir_i[d][1]*s)%N 
                temp_board[new_i][new_j].append((m,s,d))
            
    board = temp_board


def gether():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 1:
                m = sum(m for m,_,_ in board[i][j]) // 5
                if m == 0:
                    board[i][j] = []
                    continue
                s = sum(s for _,s,_ in board[i][j]) // len(board[i][j])
                if all(d%2 for _,_,d in board[i][j]) or \
                   all(d%2==0 for _,_,d in board[i][j]):
                    board[i][j] = []
                    for d in (0,2,4,6):
                        board[i][j].append((m,s,d))
                else:
                    board[i][j] = []
                    for d in (1,3,5,7):
                        board[i][j].append((m,s,d))


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    r,c,m,s,d = map(int, input().split())
    board[r-1][c-1].append((m, s, d))

for _ in range(K):
    move()
    gether()

ans = 0
for i in range(N):
    for j in range(N):
        ans += sum(m for m,_,_ in board[i][j])

print(ans)