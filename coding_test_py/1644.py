'''
백준 1644번 소수의 연속합
브루트포스 기타
'''
def prime_list(n):
    b_l = [True for _ in range(0,n+1)]
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if not b_l[i]:
            continue
        
        for j in range(i+i, n+1, i):
            b_l[j] = False

    p_l = []
    for i in range(2, n+1):
        if b_l[i]: 
            p_l.append(i)
    return p_l



n = int(input())
p_l = prime_list(n)

p, k, ans = 0, 0, 0

for temp_num in p_l:
    p += temp_num
    while p > n:
        p -= p_l[k]
        k += 1

    if p == n:
        ans += 1

print(ans)