'''
백준 19238 스타트 택시
삼성
'''
import sys

dir_i = ((-1,0), (0, -1), (1,0), (0,1)) 
def search_shortest():
    q = [(0, pos[0], pos[1])]
    visited = [[-1]*N for _ in range(N)]
    min_dist = K

    while q:
        temp_dist, temp_i, temp_j = q.pop(0)

        if temp_dist > min_dist:
            break
        
        if visited[temp_i][temp_j] >= 0:
            continue

        visited[temp_i][temp_j] = temp_dist

        if any( visited[i][j] >= 0 for i,j,_,_ in passengers):
            min_dist = temp_dist

        for ii in range(4):
            new_i = temp_i + dir_i[ii][0]
            new_j = temp_j + dir_i[ii][1]
            if new_i >= N or new_i < 0 or \
               new_j >= N or new_j < 0 or \
               visited[new_i][new_j] >= 0 or \
               board[new_i][new_j]:
                continue
            q.append((temp_dist+1, new_i, new_j))
    
    return visited

def search_shortest_():
    i, j = passengers[pass_i][2], passengers[pass_i][3]
    q = [(0, pos[0], pos[1])]
    visited = [[0]*N for _ in range(N)]

    while q:
        temp_dist, temp_i, temp_j = q.pop(0)

        if temp_dist > K:
            return False

        if visited[temp_i][temp_j]:
            continue
        visited[temp_i][temp_j] = temp_dist

        if temp_i == i and temp_j == j:
            return temp_dist

        for ii in range(4):
            new_i = temp_i + dir_i[ii][0]
            new_j = temp_j + dir_i[ii][1]
            if new_i >= N or new_i < 0 or \
               new_j >= N or new_j < 0 or \
               visited[new_i][new_j] or \
               board[new_i][new_j]:
                continue
            q.append((temp_dist+1, new_i, new_j))

def move_to_passenger():
    global K
    global pass_i

    shortest_board = search_shortest()
    dist = -1

    for idx, (i, j, _, _) in enumerate(passengers):
        if shortest_board[i][j] >= 0:
            pass_i = idx
            dist = shortest_board[i][j]
            break
    
    if dist == -1:
        return False

    pos[0], pos[1] = passengers[pass_i][0], passengers[pass_i][1]    
    K -= dist
    return True

def move_to_des():
    global K
    global pass_i

    dist = search_shortest_()
    if not dist:
        return False
    
    pos[0], pos[1] = passengers[pass_i][2], passengers[pass_i][3]
    K += dist
    return True

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

minus_1 = lambda x: int(x)-1
pos = list(map(minus_1, input().split()))
passengers = [list(map(minus_1, input().split())) for _ in range(M)]
passengers.sort(key=lambda x: (x[0], x[1]))
pass_i = 0

while passengers:
    if not move_to_passenger():
        K = -1
        break

    if not move_to_des():
        K = -1
        break
    
    del passengers[pass_i]

print(K)