'''
백준 16936번 나3곱2
'''
from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
nums_cs = Counter(nums)

def dfs(depth):
    if depth == N:
        return True
    else:
        for num in nums:
            if nums_cs[num] and \
               ((ans[-1] // 3 == num and ans[-1] % 3 == 0) or \
               ans[-1] * 2 == num):
                ans.append(num)
                nums_cs[num] -= 1
                if dfs(depth+1):
                    return True
                nums_cs[num] += 1
                ans.pop()
    return False

for num in nums:
    ans = [num]
    if dfs(1):
        break
print(' '.join(map(str, ans)))