'''
백준 2212번 센서
'''
N = int(input())
M = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
dists = [sensors[i+1] - sensors[i] for i in range(N-1)]
dists.sort()
ans = sensors[-1] - sensors[0]

for i in range(M-1):
    try:
        ans -= dists[-(1 + i)]
    except:
        break

print(ans)