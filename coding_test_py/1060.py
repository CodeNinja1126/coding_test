'''
백준 1060번 좋은 수
'''
L = int(input())
S = list(map(int, input().split()))
n = int(input())
ans = []

def count_range(a, s, e):
    c = a
    d = e - s - a
    return c * d - 1

S.sort()
temp = 0
ranges = []
for num in S:
    if num - temp <= 2:
        for i in range(temp+1, num):
            ans.append(i)
    else:
        ranges.append([1, temp, num])
    ans.append(num)
    temp = num

while len(ans) < n and ranges:
    ranges.sort(key=lambda x: (count_range(*x), x[1]))
    temp_top = ranges[0]
    if temp_top[0] + temp_top[1] == temp_top[2] - temp_top[0]:
        ans.append(temp_top[0] + temp_top[1])
        ranges = ranges[1:]
    else:
        ans.append(temp_top[0] + temp_top[1])
        ans.append(temp_top[2] - temp_top[0])
        temp_top[0] += 1
        if temp_top[0] + temp_top[1] > temp_top[2] - temp_top[0]:
            ranges = ranges[1:]

num = S[-1] + 1
while len(ans) < n:
    ans.append(num)
    num += 1

print(' '.join(map(str, ans[:n])))