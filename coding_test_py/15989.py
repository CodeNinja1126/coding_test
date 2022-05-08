'''
백준 15989번
'''

N = int(input())

for _ in range(N):
    T = int(input())
    ans = 0
    while True:
        ans += T // 2 + 1
        T -= 3
        if T < 0: break
    print(ans)
        
    