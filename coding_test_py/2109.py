'''
백준 2109번 순회강연
그리디
'''
from heapq import heappush, heappop, heapify
N = int(input())
if N == 0:
    print(0)
    exit()
    
schedule = []
for _ in range(N):
    a, b = map(int, input().split())
    a = -a
    schedule.append((a,b))
heapify(schedule)
diary = [i for i in range(max(schedule, key=lambda x:x[1])[1])]

def binary_search(val):
    left = 0
    right = len(diary)-1
    
    while(left <= right):
        middle = (left+right)//2

        if val < diary[middle]:
            right = middle - 1
        elif diary[middle] < val:
            left = middle + 1
        else:
            return middle

    return right

ans = 0
for a, b in (heappop(schedule) for _ in range(N)):
    if not diary:
        continue
    i = binary_search(b-1)
    if diary[i] > b-1:
        continue
    diary = diary[:i] + diary[i+1:]
    ans += a
    

print(-ans)
        