'''
백준 1112번 진법 변환
'''
x, b = map(int, input().split())
i = 0
ans = 0

while x != 0:
    if x > 0 and b > 0:
        n = x % b
        x = x // b
    else:
        if x % b:
            n = x % b - b
            x = x // b + 1
        else:
            n = 0
            x = x // b
    ans += n * (10 ** i)
    i += 1
print(ans)