'''
백준 12869번 뮤탈리스크
DP
'''
N = int(input())

if N == 1:
    nums = [int(input())]
    nums.append(0)
    nums.append(0)
elif N == 2:
    nums = list(map(int, input().split()))
    nums.append(0)
else:
    nums = list(map(int, input().split()))

q = [(nums, 0)]
ans = 0
while True:
    nums, at = q.pop(0)
    temp_max = max(nums)
    if nums[0] <= 0 and \
        nums[1] <= 0 and \
        nums[2] <= 0:
        ans = at
        break
    if temp_max == nums[0]:
        q.append(([nums[0]-9, nums[1]-3, nums[2]-1], at+1))
        q.append(([nums[0]-9, nums[1]-1, nums[2]-3], at+1))
    elif temp_max == nums[1]:
        q.append(([nums[0]-3, nums[1]-9, nums[2]-1], at+1))
        q.append(([nums[0]-1, nums[1]-9, nums[2]-3], at+1))
    else:
        q.append(([nums[0]-3, nums[1]-1, nums[2]-9], at+1))
        q.append(([nums[0]-1, nums[1]-3, nums[2]-9], at+1))
print(ans)