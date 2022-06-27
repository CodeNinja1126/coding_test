'''
백준 1083번 소트
'''
N = int(input())
nums = list(map(int, input().split()))
S = int(input())

ans = []
s = S
while nums:
    temp = [0, 0]
    for i, num in enumerate(nums[:s+1]):
        if temp[0] < num:
            temp[0], temp[1] = num, i
    ans.append(nums.pop(temp[1]))
    s -= temp[1]

print(' '.join(list(map(str, ans))))
