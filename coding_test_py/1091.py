'''
백준 1091번 카드 섞기
'''
N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

def shuffle(deck):
    ret = [0] * len(deck)
    for a, b in enumerate(S):
        ret[b] = deck[a]

    return ret

def check(deck):
    for a, b in enumerate(deck):
        a = a % 3
        if P[b] != a:
            return True
    else:
        return False

ans = 0
deck = [i for i in range(N)]
origin = [i for i in range(N)]

while check(deck):
    deck = shuffle(deck)
    ans += 1
    if deck == origin:
        ans = -1
        break

print(ans)