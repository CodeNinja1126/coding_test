'''
백준 2056번 작업
그래프
'''
import sys
input = sys.stdin.readline

N = int(input())
done_time_list = [0 for _ in range(N)]

for i in range(N):
    work = list(map(int,input().split()))
    temp_max = 0
    for j in work[2:]:
        temp_max = max(done_time_list[j-1], temp_max)
    done_time_list[i] = work[0] + temp_max

print(max(done_time_list))