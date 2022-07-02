'''
백준 1081번 합
'''
L, U = input().split()

dp = [0, 45]

for i in range(2, 11):
    temp = dp[i-1]
    temp *= 10
    temp += 45 * (10 ** (i-1))
    dp.append(temp)

def solution(num):
    ret = 0
    stack = []
    temp = len(num) - 1
    for i in num:
        temp_num = int(i) if temp else int(i) + 1
        ret += temp_num * dp[temp]

        for j in range(temp_num):
            ret += j * (10 ** temp)
        for j in stack:
            ret += j * temp_num * (10 ** temp)
    
        temp -= 1
        stack.append(temp_num)

    return ret

if int(L):
    L = str(int(L) - 1)
print(solution(U) - solution(L))