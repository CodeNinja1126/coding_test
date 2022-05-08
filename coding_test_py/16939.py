from copy import deepcopy

inp = list(map(int, input().split()))
cube = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(6)]

for i, num in enumerate(inp):
    j = i//4
    k = (i%4)//2
    l = (i%4)%2
    cube[j][k][l] = num

def check():
    return all( cube[i][0][0] == cube[i][0][1] == cube[i][1][0] == cube[i][1][1]  for i in range(6))


def ans():
    global cube
    origin_cube = deepcopy(cube)
    # 가로
    for i in range(2):
        # 0, 4, 2, 3
        temp, (cube[4][0][1-i], cube[4][1][1-i]) = (cube[4][0][1-i], cube[4][1][1-i]), cube[0][i]
        temp, (cube[2][1-i][0], cube[2][1-i][1])  = (cube[2][1-i][0], cube[2][1-i][1]), temp
        temp, (cube[3][0][i], cube[3][1][i]) = (cube[3][0][i], cube[3][1][i]), temp
        cube[0][i] = list(temp)
        
        if check():
            return 1

        cube = deepcopy(origin_cube)
        
    # 세로
    for i in range(2):
        # 0, 1, 2, 5
        temp, (cube[1][0][i], cube[1][1][i]) = (cube[1][0][i], cube[1][1][i]), (cube[0][0][i], cube[0][1][i])
        temp, (cube[2][0][i], cube[2][1][i]) = (cube[2][0][i], cube[2][1][i]), temp
        temp, (cube[5][0][1-i], cube[5][1][1-i]) = (cube[5][0][1-i], cube[5][1][1-i]), temp
        cube[0][0][i], cube[0][1][i] = temp

        if check():
            return 1
    
        cube = deepcopy(origin_cube)

    # 3축
    for i in range(2):
        # 3, 1, 4, 5
        temp, cube[1][i] = cube[1][i], cube[3][i]
        temp, cube[4][i] = cube[4][i], temp
        temp, cube[5][i] = cube[5][i], temp
        cube[3][i] = temp

        if check():
            return 1

        cube = deepcopy(origin_cube)

    return 0

ret = ans()
print(ret)