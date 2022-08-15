'''
백준 1050번 물약
'''
N, M = map(int, input().split())
prices = {}

for _ in range(N):
    name, cost = input().split()
    prices[name] = int(cost)

formulars = [] 
for _ in range(M):
    name, temp = input().split('=')
    temp = temp.split('+')
    formulars.append((name, temp))

for _ in range(M):
    for name, temp in formulars:
        temp_price = 0
        for mat in temp:
            if mat[1:] not in prices:
                break

            num = int(mat[0])
            temp_price += num * prices[mat[1:]]
        else:
            if name not in prices:
                prices[name] = temp_price
            else:
                prices[name] = min(prices[name], temp_price)
            
try:
    print(1000000001 if prices['LOVE'] > 1000000000 else prices['LOVE'])
except:
    print(-1)