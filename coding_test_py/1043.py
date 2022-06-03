'''
백준 1043 거짓말쟁이
'''
N, M = map(int, input().split())
awarer = list(map(int, input().split()))[1:]
temp = [0 for i in range(N+1)]
for a in awarer:
    temp[a] = 1
dp = []
dp.append((0, temp))

def compare(a, b):
    temp_set = set()
    for i in a:
        temp_set.add(b[i])
    if 2 in temp_set and 1 in temp_set:
        return False
    else:
        if 1 in temp_set:
            return True, 1
        elif 2 in temp_set:
            return True, 2
        else:
            return True, 0

for _ in range(M):
    temp_dp = []
    guests = list(map(int, input().split()))[1:]
    for num, temp_aw in dp:
        te = compare(guests, temp_aw)
        if te:
            if te[1]:
                in_aw = [te[1] if i in guests else temp_aw[i]  for i in range(N+1)]
                temp_dp.append((num+te[1]-1, in_aw))
            else:
                in_aw = [1 if i in guests else temp_aw[i]  for i in range(N+1)]
                temp_dp.append((num, in_aw))
                in_aw = [2 if i in guests else temp_aw[i]  for i in range(N+1)]
                temp_dp.append((num+1, in_aw))
        else:
            continue
        
    dp = temp_dp

print(max(dp, key=lambda x:x[0])[0])
