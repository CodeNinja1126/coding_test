'''
백준 15586번 MooTube (Gold)
'''
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())

edges = []

for _ in range(N-1):
    p, q, r = map(int, input().split())
    p -= 1
    q -= 1
    edges.append((p,q,r))

queries = []

for i in range(Q):
    k, v = map(int, input().split())
    v -= 1
    queries.append((i,k,v))

class tree:
    def __init__(self, num):
        self.num = num
        self.parent = None
        self.size = 1

    def union(self, a):
        a.parent = self
        self.size += a.size
    
    def find_root(self):
        ans = self
        tmp = self.parent
        while tmp != None:
            ans = tmp
            tmp = tmp.parent
        
        return ans

edges.sort(key=lambda x:x[2], reverse=True)
queries.sort(key=lambda x:x[1], reverse=True)
union_list = [tree(i) for i in range(N)]
ans = [0 for _ in range(Q)]

edge_idx = 0
for query in queries:
    tmp_ans = 0
    while (edge_idx < N-1) and (edges[edge_idx][2] >= query[1]):
        p, q, _ = edges[edge_idx]
        a_root = union_list[p].find_root()
        b_root = union_list[q].find_root()
        a_root.union(b_root)
        edge_idx += 1

    root = union_list[query[2]].find_root()
    ans[query[0]] = root.size - 1

for i in ans:
    print(i)