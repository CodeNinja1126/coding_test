'''
백준 1197번 최소 스패닝 트리
그래프
'''
import sys
input = sys.stdin.readline
V, E = map(int, input().split())

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

node_list = [tree(i) for i in range(V)]
edge_list = []
ans = 0

for _ in range(E):
    A,B,C = map(int, input().split())
    A -= 1
    B -= 1
    edge_list.append((A,B,C))

edge_list.sort(key=lambda x:x[2])

for A,B,C in edge_list:
    A_root = node_list[A].find_root()
    B_root = node_list[B].find_root()
    if A_root == B_root:
        continue
    if A_root.num > B_root.num:
        B_root.union(A_root)
    else: 
        A_root.union(B_root)
    ans += C
    if A_root.size == V:
        break

print(ans)
