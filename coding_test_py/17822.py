'''
백준 17822 원판 돌리기
시뮬레이션
'''
from collections import deque

N, M, T = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(N)]

ans = 0
def count():
    global ans
    for row in board:
        for num in row:
            ans += num


def rotate(i, d):
    if d:
        board[i].append(board[i].popleft())
    else:
        board[i].appendleft(board[i].pop())
        

dir_i = (0, 1)
dir_j = (1, 0)

def delete_num():
    temp_board = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue
            for k in range(2):
                new_i = i + dir_i[k]
                new_j = (j + dir_j[k]) % M
                if new_i == N:
                    continue
                if board[i][j] == board[new_i][new_j]:
                    temp_board[i][j] = True
                    temp_board[new_i][new_j] = True

    if any(any(bool for bool in row) for row in temp_board):
        for i in range(N):
            for j in range(M):
                if temp_board[i][j]:
                    board[i][j] = 0
    else:
        mean = [0, 0]
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    mean[0] += board[i][j]
                    mean[1] += 1
                    
        if mean[1]:
            mean = mean[0] / mean[1]
        else:
            mean = 0

        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    continue
                if board[i][j] > mean:
                    board[i][j] -= 1
                elif board[i][j] < mean:
                    board[i][j] += 1 
                

for _ in range(T):
    x, d, k = map(int, input().split())
    for i in range(x-1, N,x):
        for _ in range(k):
            rotate(i, d)
    delete_num()

count()
print(ans)