'''
백준 20055 컨베이어 벨트 위의 로봇
삼성
'''
def count():
    ans = 0
    for temp in indure:
        if temp == 0:
            ans += 1
    return ans

def rotate():
    indure.insert(0, indure.pop())
    robot.insert(0, robot.pop())

def drop_robot():
    if robot[-1]:
        robot[-1] = False

def robot_move():
    for i in range(N-1, -1, -1):
        if robot[i] and\
           not robot[i+1] and\
           indure[i+1]:
            robot[i], robot[i+1] = robot[i+1], robot[i]
            indure[i+1] -= 1

def lift_robot():
    if indure[0]:
        robot[0] = True
        indure[0] -= 1

N, K = map(int, input().split())
indure = list(map(int, input().split()))
robot = [False for _ in range(N)]

ret = 0
while count() < K:
    ret += 1
    rotate()
    drop_robot()
    robot_move()
    drop_robot()
    lift_robot()

print(ret)