'''
백준 21609번 주사위 굴리기2
삼성
'''
class dice():
    def __init__(self):
        self.m = [2, 1, 5, 6, 4, 3]
    
    def __roll(self):
        self.m[0], self.m[1], self.m[2], self.m[3] = \
            self.m[3], self.m[0], self.m[1], self.m[2]
    
    def __turn(self):
        self.m[0], self.m[5], self.m[2], self.m[4] = \
            self.m[4], self.m[0], self.m[5], self.m[2]
    
    def turn_clock(self):
        self.__turn()
    
    def turn_anti_clock(self):
        self.__turn()
        self.__turn()
        self.__turn()
    
    def roll(self, dir, cycle):
        cycle = cycle % 4
        for _ in range(dir):
            self.turn_anti_clock()
        for _ in range(cycle):
            self.__roll()
        for _ in range(dir):
            self.turn_clock()

di = dice()
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dir_i = 3
dirs = ((1,0), (0, -1), (-1,0), (0,1))
x, y = 0, 0
ans = 0

def dfs(x, y, b):
    visited[x][y] = True
    for i in range(4):
        new_x, new_y = x+dirs[i][0], y+dirs[i][1]
        if new_x >= 0 and new_y >= 0 and\
           new_x < N and new_y < M and\
           board[new_x][new_y] == b and\
           visited[new_x][new_y] == False :
            dfs(new_x, new_y, b)


for _ in range(K):
    new_x, new_y = x+dirs[dir_i][0], y+dirs[dir_i][1]
    
    if new_x < 0 or new_y < 0 or\
       new_x >= N or new_y >= M:
        dir_i = (dir_i + 2) % 4
        x, y = x+dirs[dir_i][0], y+dirs[dir_i][1]
    else:
        x, y = new_x, new_y
        
    di.roll(dir_i, 1)
    B = board[x][y]
    visited = [[False for _ in range(M)] for _ in range(N)]
    dfs(x, y, B)
    point = sum(sum(1 if val == True else 0 for val in row) for row in visited)
    ans += B * point
    A = di.m[3]
    if A > B:
        dir_i = (dir_i + 1) % 4
    elif A < B:
        dir_i = (dir_i + 3) % 4

print(ans)
