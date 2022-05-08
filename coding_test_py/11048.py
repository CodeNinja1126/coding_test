'''
백준 11048번 이동하기
DP
'''
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir_i = ((0,-1), (-1,-1), (-1,0))

for i in range(N):
    for j in range(M):
        score = 0
        for k in range(3):
            pos_i = dir_i[k][0] + i
            pos_j = dir_i[k][1] + j
            if pos_i < 0 or \
               pos_j < 0 or \
               pos_i >= N or \
               pos_j >= M:
                continue
            else:
                score = max(score, board[pos_i][pos_j])
        board[i][j] += score

print(board[N-1][M-1])