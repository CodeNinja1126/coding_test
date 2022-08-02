'''
백준 1092번 배
'''
N = int(input())
cranes = list(map(int, input().split()))
cranes.sort()
M = int(input())
cargos = list(map(int, input().split()))
cargos.sort()

if cranes[-1] < cargos[-1]:
    print(-1)
else:
    cargos.reverse()
    temp_dict = [0] * len(cranes)
    for cargo in cargos:
        for i, crane in enumerate(cranes[:-1]):
            if temp_dict[i+1] > temp_dict[i] and\
               crane >= cargo:
                temp_dict[i] += 1
                break
        else:
            temp_dict[-1] += 1
         
    ans = temp_dict[-1]


    '''
    temp_dict = [0] * len(cranes)
    j = 0
    for i in cargos:
        for idx, j in enumerate(cranes):
            if i <= j:
                temp_dict[idx] += 1
    ans = 0
    while temp_dict[-1] > 0:
        for i in range(len(cranes)):
            for j in range(i, len(cranes)):
                if temp_dict[j] == 0:
                    break
                temp_dict[j] -= 1
        ans += 1
    '''
    print(ans)