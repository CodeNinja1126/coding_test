'''
백준 16974번 레벨 햄버거
시뮬레이션 구현
'''
N, X = map(int, input().split())

w_num = [1]
p_num = [1]

for _ in range(N):
    w_num.append(w_num[-1]*2 + 2 + 1)
    p_num.append(p_num[-1]*2 + 1)

def recursive(X,d):
    if d == 0:
        return 1
    elif X == 0:
        return 0
    elif X < w_num[d]//2:
        return recursive(X-1, d-1)
    elif X == w_num[d]//2:
        return 1 + p_num[d-1]
    elif X < w_num[d]-1:
        return 1 + p_num[d-1] + recursive(X-1-(w_num[d]//2), d-1)
    elif X == w_num[d]-1:
        return p_num[d]

print(recursive(X-1,N))