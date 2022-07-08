'''
백준 1099번 알수없는 문장
'''
from sys import maxsize

phrase = input()
N = int(input())
words = [input() for _ in range(N)]
ordered_words = []
for word in words:
    ordered_words.append(sorted(word))

dp = [maxsize for _ in range(len(phrase)+1)]
dp[-1] = 0

for i in range(len(phrase)):
    for word, ordered_word in zip(words, ordered_words):
        sub_ph = phrase[i-len(word) + 1:i+1]
        if i - len(word) + 1 < 0 or\
           dp[i - len(word)] == maxsize or\
           sorted(sub_ph) != ordered_word:
            continue
        temp_p = 0
        for ch_1, ch_2 in zip(word, sub_ph):
            if ch_1 != ch_2:
                temp_p += 1
        dp[i] = min(dp[i], temp_p+dp[i - len(word)])

if dp[-2] == maxsize:
    print(-1)
else:
    print(dp[-2])
