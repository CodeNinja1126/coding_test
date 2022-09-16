'''
프로그래머스 등산코스 정하기
카카오
'''
from collections import defaultdict

def solution(n, paths, gates, summits):
    graph = defaultdict(lambda:{})
    visited = [10000001 for i in range(n+1)]
    ans = [6000000,10000001]
    for i,j,w in paths:
        graph[i][j] = w
        graph[j][i] = w
    

    sum_list = [False for _ in range(n+1)]
    for summ in summits:
        sum_list[summ] = True
    
    q = gates
    for g in q:
        visited[g] = 0
    
    while q:
        tmp_q = []
        for v in q:
            if sum_list[v]:
                continue
                
            for k, val in graph[v].items():
                tmp = max(visited[v],val)
                if val <= ans[1] and visited[k] > tmp:
                    visited[k] = tmp
                    tmp_q.append(k)
        q = tmp_q
        
    for summ in summits:
        if ans[1] > visited[summ]:
            ans[0] = summ
            ans[1] = visited[summ]
        
    return ans