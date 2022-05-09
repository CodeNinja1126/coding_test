from collections import Counter

R, C, K = map(int, input().split())
R -= 1
C -= 1

A = [list(map(int, input().split())) for _ in range(3)]

def cus_sort(li):
    temp = Counter(li[:100])
    t_temp = []
    for it in temp.items():
        if it[0] != 0:
            t_temp.append(it)
    temp = t_temp
    temp.sort(key=lambda x:(x[1], x[0]))
    t_temp = []
    for a, b in temp:
        t_temp.append(a)
        t_temp.append(b)
    return t_temp

def cal_r():
    global A
    temp_A = []
    max_len = 0
    for row in A:
        temp = cus_sort(row)
        max_len = max(max_len, len(temp))
        temp_A.append(temp)

    for row in temp_A:
        if len(row) < max_len:
            row += [0] * (max_len - len(row))
    
    A = temp_A
        

def cal_c():
    global A
    temp_A = []
    max_len = 0
    for i in range(len(A[0])):
        col = [row[i] for row in A]
        temp = cus_sort(col)
        max_len = max(max_len, len(temp))
        temp_A.append(temp)

    for row in temp_A:
        if len(row) < max_len:
            row += [0] * (max_len - len(row))

    t_temp_A = [[0 for _ in range(len(temp_A))] for _ in range(len(temp_A[0]))]

    for i, row in enumerate(temp_A):
        for j, num in enumerate(row):
            t_temp_A[j][i] = num

    A = t_temp_A

for i in range(101):
    if R < len(A) and \
       C < len(A[0]) and \
       A[R][C] == K:
        print(i) 
        break
    if len(A) >= len(A[0]):
        cal_r()
    else:
        cal_c()
else:
    print(-1)