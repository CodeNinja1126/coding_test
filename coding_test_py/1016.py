'''
백준 1016번 제곱ㄴㄴ수
'''

min_n, max_n = map(int, input().split())
squared = [False for _ in range(max_n - min_n + 1)]

for i in range(2, 1000001):
    temp_squared = i**2

    if temp_squared > max_n:
        break
    
    remainder = min_n % temp_squared
    remainder = 1 if remainder else 0
    temp_min = (min_n // temp_squared + remainder) * temp_squared

    if temp_min > max_n:
        continue

    for j in range(1000001): 
        try:
            squared[temp_min-min_n + j*temp_squared] = True
        except:
            break

ans = 0
for val in squared:
    if val == False:
        ans += 1

print(ans)
