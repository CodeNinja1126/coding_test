'''
백준 21608번 상어 초등학교
삼성 sw 문제
'''
N = int(input())
seats = [[0 for __ in range(N)] for _ in range(N)]
stus = []
stus_dict = {}
dir_i = ((0,1),(1,0),(0,-1),(-1,0))

def teacher(stu):
    pos_i, pos_j = 0, 0
    score = -1
    for i in range(N):
        for j in range(N):
            temp_score = 0
            if seats[i][j]:
                continue
            for k in range(4):
                new_pos_i, new_pos_j = dir_i[k][0] + i, dir_i[k][1] + j
                if new_pos_i < 0 or \
                   new_pos_j < 0 or \
                   new_pos_i >= N or \
                   new_pos_j >= N:
                    continue
                elif seats[new_pos_i][new_pos_j] in stus_dict[stu]:
                    temp_score += 10
                elif seats[new_pos_i][new_pos_j] == 0:
                    temp_score += 1
            if temp_score > score:
                score = temp_score
                pos_i,pos_j = i, j
    
    return pos_i, pos_j

def cal_sat(i, j):
    score = 0
    for k in range(4):
        new_pos_i, new_pos_j = dir_i[k][0] + i, dir_i[k][1] + j
        if new_pos_i < 0 or \
            new_pos_j < 0 or \
            new_pos_i >= N or \
            new_pos_j >= N:
            continue
        if seats[new_pos_i][new_pos_j] in stus_dict[seats[i][j]]:
            score += 1
            
    if score:
        score = 10 ** (-1+score)
    
    return score
    

for _ in range(N*N):
    temp_list = list(map(int, input().split()))
    stus.append(temp_list[0])
    stus_dict[temp_list[0]] = temp_list[1:]


for stu in stus:
    pos_i, pos_j = teacher(stu)
    seats[pos_i][pos_j] = stu

ans = 0
for i in range(N):
    for j in range(N):
        ans += cal_sat(i,j)

print(ans)