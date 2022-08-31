'''
백준 17282번 우주탐사선 
'''
N, K = map(int, input().split())

dist = []
for _ in range(N):
    dist.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            dist[i][k] = min(dist[i][k], dist[i][j] + dist[j][k])

ans = 100000
visited = 0
now_time = 0
full_visited = 0
for i in range(N):
    full_visited += 1 << i

def dfs(pre_pos):
    global ans, visited, now_time
    if visited == full_visited:
        ans = min(ans, now_time)
    else:
        for i in range(N):
            if visited & (1 << i) != 1 << i:
                visited += 1 << i
                now_time += dist[pre_pos][i] 
                dfs(i)
                now_time -= dist[pre_pos][i] 
                visited -= 1 << i

visited += 1 << K
dfs(K)
print(ans)