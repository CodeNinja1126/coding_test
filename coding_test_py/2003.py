'''
백준 2003번 수들의 합 2
브루트포스 기타
'''
N, M = map(int, input().split())
A = list(map(int, input().split()))

combi_list = []

ans = 0
p = 0
k = 0

for temp_num in A:
    p += temp_num
    while p > M:
        p -= A[k]
        k += 1

    if p == M:
        ans += 1

print(ans)