'''
백준 15686번 치킨 배달
브루트 포스
'''
N, M = map(int, input().split())
house = []
store = []
for i in range(N):
    for j, building in enumerate(input().split()):
        if building == '1':
            house.append((i,j))
        elif building == '2':
            store.append((i,j))

dist_map = [[0] * len(store) for _ in range(len(house))]

for i in range(len(house)):
    for j in range(len(store)):
        dist_map[i][j] = abs(house[i][0] - store[j][0]) + \
                         abs(house[i][1] - store[j][1])

ans = 100000

combi = []
def combination(depth):
    global ans
    if depth > len(store):
        return
    elif len(combi) == M:
        temp = 0
        for i in range(len(house)):
            temp += min(dist_map[i][j] for j in combi)
        ans = min(temp, ans)
    else:
        combination(depth+1)
        combi.append(depth)
        combination(depth+1)
        combi.pop()

combination(0)
print(ans)