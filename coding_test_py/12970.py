'''
백준 12970번 AB
그리디
'''
N, M = map(int, input().split())

ans = ''
tu_num = 0
A_num = 0

for i in range(N):
    if tu_num < M:
        if tu_num - A_num + N - i - 1 <= M:
            ans += 'A'
            tu_num += - A_num + N - i - 1
            A_num += 1
        else:
            ans += 'B'
    else:
        ans += 'B'


if M == tu_num:
    print(ans)
else:
    print(-1)