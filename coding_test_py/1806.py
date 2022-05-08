'''
백준 1806번 부분합
브루트포스 기타
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))

p, k, len, ans = 0, 0, 1, 1000000

for num in A:
    flg = 0
    p += num
    len += 1
    while p >= M:
        flg = 1
        p -= A[k]
        k += 1
        len -= 1
    if flg:
        ans = min(len, ans)

if ans == 1000000:
    print(0)
else:
    print(ans)