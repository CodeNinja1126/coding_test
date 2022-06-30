'''
백준 1089번 스타트링크 타워
'''

N = int(input())

num_l = [
    [[1,1,1], # 0
     [1,0,1],
     [1,0,1],
     [1,0,1],
     [1,1,1]
    ],
    [[0,0,1], # 1
     [0,0,1],
     [0,0,1],
     [0,0,1],
     [0,0,1]
    ],
    [[1,1,1], # 2
     [0,0,1],
     [1,1,1],
     [1,0,0],
     [1,1,1]
    ],
    [[1,1,1], # 3
     [0,0,1],
     [1,1,1],
     [0,0,1],
     [1,1,1]
    ],
    [[1,0,1], # 4
     [1,0,1],
     [1,1,1],
     [0,0,1],
     [0,0,1]
    ],
    [[1,1,1], # 5
     [1,0,0],
     [1,1,1],
     [0,0,1],
     [1,1,1]
    ],
    [[1,1,1], # 6
     [1,0,0],
     [1,1,1],
     [1,0,1],
     [1,1,1]
    ],
    [[1,1,1], # 7
     [0,0,1],
     [0,0,1],
     [0,0,1],
     [0,0,1]
    ],
    [[1,1,1], # 8
     [1,0,1], 
     [1,1,1],
     [1,0,1],
     [1,1,1]
    ],
    [[1,1,1], # 9
     [1,0,1],
     [1,1,1],
     [0,0,1],
     [1,1,1]
    ]
]

screen = [input() for _ in range(5)]
num = []

def check(index):
    ret = []
    for i in range(10):
        for j in range(5):
            for k in range(3):
                if screen[j][index+k] == '#' and\
                   num_l[i][j][k] == 0:
                   break
            else:
                continue
            break
        else:
            ret.append(i)
    if ret:
        return ret
    else:
        return -1

for i in range(0,len(screen[0]),4):
    temp = check(i)
    if temp == -1:
        break
    num.append(temp)

ans = 0
if temp == -1:
    print(-1)
else:
    for i, temp_num in enumerate(num[::-1]):
        ans += (sum(temp_num)/len(temp_num))*(10**i)
    print(ans)