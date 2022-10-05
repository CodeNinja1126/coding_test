'''
백준 1580번 위치 바꾸기
그래프
'''
import sys
from collections import deque
N, M = map(int, input().split())
board = []
posit= []
for i in range(N):
    tmp = []
    for j, ch in enumerate(input()):
        if ch == 'A' or ch == 'B':
            tmp.append('.')
            posit.append((i,j))
        else:
            tmp.append(ch)
    board.append(tmp)

dirs = ((0,0),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))

visit = [[False for _ in range(N*M)] for _ in range(N*M)]
visit[posit[0][0]*M+posit[0][1]][posit[1][0]*M+posit[1][1]] = True
q = deque()
q.append((posit, 0))
while q:
    (a_pos, b_pos), turn = q.popleft()

    if a_pos == posit[1] and\
       b_pos == posit[0]:
        print(turn)
        break

    for d_i in range(9):
        new_a_i = a_pos[0] + dirs[d_i][0]
        new_a_j = a_pos[1] + dirs[d_i][1]

        if new_a_i < 0 or new_a_i >= N or\
           new_a_j < 0 or new_a_j >= M or\
           board[new_a_i][new_a_j] == 'X':
            continue

        for d_j in range(9):
            new_b_i = b_pos[0] + dirs[d_j][0]
            new_b_j = b_pos[1] + dirs[d_j][1]

            if new_b_i < 0 or new_b_i >= N or\
               new_b_j < 0 or new_b_j >= M or\
               board[new_b_i][new_b_j] == 'X':
                continue

            tmp_a = (new_a_i, new_a_j)
            tmp_b = (new_b_i, new_b_j)

            if tmp_a == a_pos and\
               tmp_b == b_pos:
                continue

            if tmp_a == b_pos and\
               tmp_b == a_pos:
                continue
            
            if tmp_a == tmp_b:
                continue

            if visit[new_a_i*M+new_a_j][new_b_i*M+new_b_j]:
                continue

            visit[new_a_i*M+new_a_j][new_b_i*M+new_b_j] = True

            q.append(((tmp_a, tmp_b), turn+1))

else:
    print(-1)
