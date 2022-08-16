'''
백준 16953번 A -> B
'''
a, b = map(int, input().split())
ans = 0
while a < b:
    ans += 1
    if str(b)[-1] == '1':
        b = int(str(b)[:-1])
    elif b % 2:
        break
    else:
        b //= 2

if a == b:
    print(ans+1)
else:
    print(-1)
    