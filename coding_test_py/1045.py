'''
백준 1045번 도로
'''
N, M = map(int, input().split())
roads = []
graph = dict()

for i in range(N):
    row = input()
    for j, yn in enumerate(row[i:]):
        if yn == 'Y':
            roads.append((i, j+i))

ans = [0 for _ in range(N)]
linked_set = set()
linked_set.add(0)

flg = False

for i in range(M):
    if len(linked_set) < N:
        for j in range(len(roads)):
            a, b = roads[j]
            if a in linked_set and\
               b in linked_set:
                continue
            elif a in linked_set or\
                 b in linked_set:
                ans[a] += 1
                ans[b] += 1
                linked_set.add(a)
                linked_set.add(b)
                roads.pop(j)
                break
        else:
            break
    else:
        try:
            a, b = roads[0]
            ans[a] += 1
            ans[b] += 1
            roads.pop(0)
        except:
            break
else:
    flg = True

if flg:
    print(' '.join(map(str, ans)))
else:
    print(-1)