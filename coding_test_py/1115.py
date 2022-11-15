'''
백준 1115번 순열
'''
N = int(input())
li = list(map(int, input().split()))
visited = [False for _ in range(N)]

def dfs(d):
    if visited[d]:
        return
    else:
        visited[d] = True
        dfs(li[d])

ans = 0
for i in range(N):
    if not visited[i]:
        ans += 1
        dfs(i)

if ans == 1:
    ans = 0
print(ans)