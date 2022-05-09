from math import sqrt

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if x1 == x2 and\
       y1 == y2 and\
       r1 == r2:
        print(-1)
    elif dist > float(r1 + r2):
        print(0)
    elif dist == float(r1 + r2):
        print(1)
    elif (dist < r1 and dist == float(r1-r2)) or \
         (dist < r2 and dist == float(r2-r1)):
        print(1)
    elif (dist < r1 and dist < float(r1-r2)) or \
         (dist < r2 and dist < float(r2-r1)):
        print(0)
    else:
        print(2)
    