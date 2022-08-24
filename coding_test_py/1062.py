'''
백준 1062번 가르침
'''
import sys
from collections import Counter
input = sys.stdin.readline
N, K = map(int, input().split())
if K < 5:
    print(0)
    exit()

def ch2idx(ch):
    return (ord(ch) - ord('a'))

vocab = 0
for ch in 'antic':
    vocab += 1 << ch2idx(ch)

words = []
for _ in range(N):
    word = input()[4:-4]
    temp = 0
    for ch in Counter(word).keys():
        temp += 1 << ch2idx(ch)
    words.append(temp)

ans = 0
n_vocab = 5
teachable = 'bdefghjklmopqrsuvwxyz'

def dfs(depth):
    global ans
    global n_vocab
    global vocab

    if n_vocab == K:
        tmp = 0
        for bits in words:
            tmp += 1 if vocab & bits == bits else 0
        ans = max(ans, tmp)
    elif depth == 21:
        return
    else:
        dfs(depth+1)
        n_vocab += 1
        vocab += 1 << ch2idx(teachable[depth])
        dfs(depth+1)
        n_vocab -= 1
        vocab -= 1 << ch2idx(teachable[depth])

dfs(0)
print(ans)

