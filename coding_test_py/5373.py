'''
백준 5373번 큐빙
삼성
'''
T = int(input())

def cube_init():
    return [
        [['w', 'w', 'w'], # 윗면
         ['w', 'w', 'w'],
         ['w', 'w', 'w']
        ],
        [['r', 'r', 'r'], # 앞면
         ['r', 'r', 'r'],
         ['r', 'r', 'r']
        ],
        [['y', 'y', 'y'], # 아랫면
         ['y', 'y', 'y'],
         ['y', 'y', 'y']
        ],
        [['o', 'o', 'o'], # 뒷면
         ['o', 'o', 'o'],
         ['o', 'o', 'o']
        ],
        [['g', 'g', 'g'], # 왼쪽면
         ['g', 'g', 'g'],
         ['g', 'g', 'g']
        ],
        [['b', 'b', 'b'], # 오른쪽면
         ['b', 'b', 'b'],
         ['b', 'b', 'b']
        ],
    ]

def doll(square, dir_flg):
    temp = [[0,0,0] for _ in range(3)]
    for i, row in enumerate(square[::-dir_flg]):
        for j, num in enumerate(row[::dir_flg]):
            temp[j][i] = num
    return temp


def rotate():
    global cube
    temp = [0,0,0,0,0,0]
    temp[1] = cube[5]
    temp[4] = cube[1]
    temp[5] = doll(cube[3], 1)
    temp[5] = doll(temp[5], 1)
    temp[3] = doll(cube[4], 1)
    temp[3] = doll(temp[3], 1)
    temp[0] = doll(cube[0], 1)
    temp[2] = doll(cube[2], -1)
    cube = temp


def roll():
    global cube
    temp = [0,0,0,0,0,0]
    temp[0] = cube[3]
    temp[1] = cube[0]
    temp[2] = cube[1]
    temp[3] = cube[2]
    temp[4] = doll(cube[4], 1)
    temp[5] = doll(cube[5], -1)
    cube = temp


def change(move):
    if move[0] == 'F':
        rotate()
    elif move[0] == 'B':
        rotate()
        rotate()
        rotate()
    elif move[0] == 'D':
        roll()
        rotate()
        rotate()
        rotate()
    elif move[0] == 'R':
        rotate()
        rotate()
    elif move[0] == 'U':
        roll()
        rotate()
    
    if move[1] == '-':
        cube[4] = doll(cube[4], -1)
        temp = [cube[3][0][0],cube[3][1][0],cube[3][2][0]]
        for i in [2,1,0,3]:
            for j in range(3):
                cube[i][j][0],temp[j] = temp[j], cube[i][j][0]
    else:
        cube[4] = doll(cube[4], 1)
        temp = [cube[3][0][0],cube[3][1][0],cube[3][2][0]]
        for i in range(4):
            for j in range(3):
                cube[i][j][0],temp[j] = temp[j], cube[i][j][0]

    if move[0] == 'F':
        rotate()
        rotate()
        rotate()
    elif move[0] == 'B':
        rotate()
    elif move[0] == 'D':
        rotate()
        roll()
        roll()
        roll()
    elif move[0] == 'R':
        rotate()
        rotate()
    elif move[0] == 'U':
        rotate()
        rotate()
        rotate()
        roll()
        roll()
        roll()


for _ in range(T):
    cube = cube_init()
    N = int(input())
    move_list = list(input().split())
    for move in move_list:
        change(move)
    print(''.join(cube[0][0]))
    print(''.join(cube[0][1]))
    print(''.join(cube[0][2]))
