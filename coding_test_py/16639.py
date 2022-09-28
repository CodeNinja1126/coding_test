'''
백준 16639번 괄호 추가하기 3
DP
'''
input()
f = input()
nums = []
ops = []
for ch in f:
    if ord('0') <= ord(ch) <= ord('9'):
        nums.append(int(ch))
    else:
        ops.append(ch)

def mul(a, b): return a * b
def add(a, b): return a + b
def sub(a, b): return a - b
op_dict = {}
op_dict['*'] = mul
op_dict['+'] = add
op_dict['-'] = sub

matrix = [[[-2**31, 2**31] for _ in range(len(nums))] for _ in range(len(nums))]
for i in range(len(nums)):
    matrix[i][i] = ([nums[i],nums[i]])


for idx, j in enumerate(range(1, len(nums))):
    idx += 2
    for i in range(len(nums)-j):
        for m in range(1,idx):
            for k in matrix[i][j-m]:
                for l in matrix[i+(idx-m)][j]:
                    val = op_dict[ops[j-m]](k,l)
                    matrix[i][j][0] = max(matrix[i][j][0], val)
                    matrix[i][j][1] = min(matrix[i][j][1], val)
    
        j += 1


print(matrix[0][-1][0])