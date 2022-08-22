'''
백준 2812번 크게 만들기
그리디
'''
_, a = map(int, input().split())
N = list(input())

flg = 0
i = 0
ans = []
while i < len(N):
    if ans and \
       ans[-1] < N[i] and \
       flg < a:
        ans.pop()
        flg += 1
    else:
        ans.append(N[i])
        i += 1

if a > flg:
    ans = ans[:-(a-flg)]

print(''.join(ans))