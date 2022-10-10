'''
백준 1101번 카드 정리 1
'''
N, M = map(int, input().split())
flg = False
done_list = [False for _ in range(M)]
ans = 0
for _ in range(N):
    box = list(map(int, input().split()))
    total = sum(box)
    if total == 0:
        continue

    for i, cards in enumerate(box):
        if cards == total:
            if done_list[i]:
                ans += 1
                if not flg:
                    ans -= 1
                    flg = not flg
                break
            done_list[i] = True
            break
    else:
        ans += 1
        if not flg:
            ans -= 1
            flg = not flg

print(ans)