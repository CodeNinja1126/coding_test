'''
백준 1025 제곱수 찾기
DP
'''
from math import sqrt

N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
ans = -1

for i in range(N):
    for j in range(M):
        for k in range(-N+1, N):
            for l in range(-M+1, M):
                if k == 0 and l == 0:
                    if not (sqrt(board[i][j]) % 1.0):
                        ans = max(board[i][j], ans)
                    continue
                num = str(board[i][j])
                iter = 1
                while 1:
                    new_i = i + k * iter
                    new_j = j + l * iter
                    if new_i < 0 or new_i >= N or\
                       new_j < 0 or new_j >= M:
                       break
                    num += str(board[new_i][new_j])
                    temp = int(num)
                    if not (sqrt(temp) % 1.0):
                        ans = max(temp, ans)
                    iter += 1

print(ans)