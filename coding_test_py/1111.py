'''
백준 1111번 IQ테스트
'''
N = int(input())
nums = list(map(int, input().split()))

if N == 1:
    print('A')
elif N == 2:
    if nums[0] == nums[1]:
        print(nums[0])
    else:
        print('A')
else:
    ans = 'B'
    try:
        a = (nums[2] - nums[1]) // (nums[1] - nums[0])
    except:
        a = 0
    for i in range(1, len(nums)-2):
        try:
            temp_a = (nums[i+2] - nums[i+1]) // (nums[i+1] - nums[i])
        except:
            temp_a = 0
        if a != temp_a:
            break
    else:
        b = nums[1] - a*nums[0]
        for i in range(1, len(nums)):
            if nums[i] != a*nums[i-1] + b:
                break
        else:
            ans = a*nums[-1] + b
    print(ans)
