'''
백준 16936번 나3곱2
'''
from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
nums_cs = Counter(nums)

'''brute-force
def dfs(depth):
    if depth == N:
        return True
    else:
        for num in ans[-1] // 3, ans[-1] * 2:
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
    nums_cs[num] -= 1
    if dfs(1):
        break
    nums_cs[num] += 1
'''
# topology sort

for num in nums:
    if nums_cs[num*2]:
        continue
    if num % 3 == 0 and nums_cs[num//3]:
        continue
    end_num = num
    break

ans = [end_num]
while len(ans) < N:
    if ans[-1] % 2 == 0 and nums_cs[ans[-1]//2]:
        ans.append(ans[-1]//2)
    else:
        ans.append(ans[-1]*3)

ans.reverse()
print(' '.join(map(str, ans)))