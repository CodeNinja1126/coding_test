'''
백준 1030 프랙탈 평면
'''

def cell_color(s, i, j):
    if s == 0:
        return 0
    else:
        leng = N ** (s - 1)
        sp = leng*((N - K) // 2)
        ep = N ** s - sp
        if ep > i >= sp and\
           ep > j >= sp:
            return 1
        else:
            i %= leng
            j %= leng
            return cell_color(s-1, i, j)

s, N, K, R1, R2, C1, C2 = map(int, input().split())

for i in range(R1, R2+1):
    print(''.join(str(cell_color(s, i, j)) for j in range(C1, C2+1)))
