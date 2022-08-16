'''
백준 17779번 게리맨더링 2
삼성
'''
from sys import maxsize
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

def check(x, y, d1, d2):
    temp = [[0]*N for _ in range(N)]
    leng = x+1
    for i in range(y+d1):
        for j in range(leng):
            temp[i][j] = 1
        if i+1 >= y:
            leng -= 1
    
    leng = N - x - 1
    for i in range(y+d2+1):
        for j in range(N-leng, N):
            temp[i][j] = 2
        if i >= y:
            leng -= 1

    leng = x - d1
    for i in range(y+d1,N):
        for j in range(leng):
            temp[i][j] = 3
        if i < y+d2+d1:
            leng += 1
    
    leng = N - x - d2
    for i in range(y+d2+1, N):
        for j in range(N-leng,N):
            temp[i][j] = 4
        if i <= y+d2+d1:
            leng += 1

    peoples = [0, 0, 0, 0, 0]
    for i in range(N):
        for j in range(N):
            peoples[temp[i][j]] += A[i][j]
    
    return max(peoples) - min(peoples)

ans = maxsize

for x in range(1,N-1):
    for y in range(1,N-1):
        for d1 in range(1,N-1):
            for d2 in range(1,N-1):
                if x + d2 >= N or y + d2 >= N or \
                   x - d1 < 0 or y + d1 >= N or \
                   y + d1 + d2 >= N:
                    continue
                ans = min(check(x, y, d1, d2), ans)

print(ans)