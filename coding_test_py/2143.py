'''
백준 1208번 두 배열의 합
브루트포스 기타
'''
from collections import defaultdict

T = int(input())
N = int(input())
A = map(int, input().split())
M = int(input())
B = map(int, input().split())
sum_A = defaultdict(int)
ans = 0

temp_sum = []
for num in A:
    for i in range(len(temp_sum)):
        temp_sum[i] += num
    temp_sum.append(num)
    for i in temp_sum:
        sum_A[i] += 1

temp_sum = []
for num in B:
    for i in range(len(temp_sum)):
        temp_sum[i] += num
    temp_sum.append(num)
    for i in temp_sum:
        ans += sum_A[T - i]

print(ans)