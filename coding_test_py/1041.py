'''
백준 1041 주사위
'''
import sys

N = int(input())
A, B, C, D, E, F = map(int, input().split())

def count_3():
    ret = sys.maxsize
    ret = min(ret, A + B + C)
    ret = min(ret, A + C + E)
    ret = min(ret, A + E + D)
    ret = min(ret, A + D + B)
    ret = min(ret, F + B + C)
    ret = min(ret, F + C + E)
    ret = min(ret, F + E + D)
    ret = min(ret, F + D + B)
    return ret

def count_2():
    ret = sys.maxsize
    ret = min(ret, A + B)
    ret = min(ret, A + C)
    ret = min(ret, A + D)
    ret = min(ret, A + E)
    ret = min(ret, B + C)
    ret = min(ret, C + E)
    ret = min(ret, E + D)
    ret = min(ret, D + B)
    ret = min(ret, F + B)
    ret = min(ret, F + C)
    ret = min(ret, F + D)
    ret = min(ret, F + E)
    return ret

if N == 1:
    print(sum((A, B, C, D, E, F)) - max(A, B, C, D, E, F))
else:
    ans = 4 * count_3() + \
          4 * (N - 1) * count_2() + \
          4 * (N - 2) * count_2() + \
          (N - 2) * (N - 2) * min(A, B, C, D, E, F) + \
          4 * (N - 2) * (N - 1) * min(A, B, C, D, E, F)
    print(ans)