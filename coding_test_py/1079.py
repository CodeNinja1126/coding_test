'''
백준 1079번 마피아
브루트 포스
'''
N = int(input())
score = list(map(int, input().split()))
weights = [list(map(int, input().split())) for _ in range(N)]
me = int(input())
ans = 0

def dfs(depth):
    global ans
    if depth == N - 1 or\
       score[me] == 0:
        return
    else:
        if (N - depth) % 2:
            temp_score = max(score)
            i = score.index(max(score))
            score[i] = 0
            dfs(depth+1)
            score[i] = temp_score
        else:
            ans = max(ans, depth//2+1)
            for i in range(N):
                if score[i]:
                    temp_score = score[i]
                    score[i] = 0
                    for j in range(N):
                        if score[j]:
                            score[j] += weights[i][j]
                    dfs(depth+1)
                    for j in range(N):
                        if score[j]:
                            score[j] -= weights[i][j]
                    score[i] = temp_score

dfs(0)
print(ans)