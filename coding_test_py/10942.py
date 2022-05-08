'''
백준 10942 팰린드롬?
DP 
'''
import sys

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
palin_li = [['0\n' for _ in range(2001)] for _ in range(2001)]

for i in range(N):
    for j in range(N):
        if i+j >= N or \
           i-j < 0:
            break
        if nums[i+j] != nums[i-j]:
            break
        palin_li[i-j+1][i+j+1] = '1\n'
        
    for j in range(N):
        if i+j+1 >= N or \
           i-j < 0:
            break
        if nums[i+j+1] != nums[i-j]:
            break
        palin_li[i-j+1][i+j+2] = '1\n'

for _ in range(M):
    S, E = map(int,sys.stdin.readline().split())
    sys.stdout.write(palin_li[S][E])