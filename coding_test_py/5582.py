'''
백준 5582번 공통 부분 문자열
DP
'''
A = input()
B = input()
A, B = sorted((A, B), key=lambda x:len(x))
ans = 0
for i in range(len(A)-1,-1,-1):
    tmp = 0
    for j, ch in enumerate(A[i:]):
        if B[j] == ch:
            tmp += 1
        else:
            tmp = 0
        ans = max(ans , tmp)

for i in range(len(B)):
    tmp = 0
    for j, ch in enumerate(A[:len(B)-i]):
        if B[i+j] == ch:
            tmp += 1
        else:
            tmp = 0
        ans = max(ans , tmp)
            
print(ans)