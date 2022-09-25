'''
백준 14890번 경사로
삼성
'''
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def road(row):
    tmp = row[0]
    ret = [0 for _ in range(N)]
    for i in range(1, N):
        if tmp == row[i]:
            continue
        elif tmp+1 == row[i]:
            if i - L >= 0 and\
               all(num == tmp for num in row[i-L:i]) and\
               not any(ret[i-L:i]):
                for num in range(i-L, i):
                    ret[num] = 1
            else:
                return False
            tmp += 1
        elif tmp-1 == row[i]:
            if i + L <= N and\
               all(num == tmp-1 for num in row[i:i+L]) and\
               not any(ret[i:i+L]):
                for num in range(i,i+L):
                    ret[num] = 1
            else:
                return False
            tmp -= 1
        else:
            return False
    
    return True

ans = 0

for i in range(N):
    if road(board[i]):
        ans += 1

for j in range(N):
    if road([board[i][j] for i in range(N)]):
        ans += 1

print(ans)