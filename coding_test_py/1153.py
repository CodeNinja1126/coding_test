'''
백준 1153번 네개의 소수
'''
def prime(N):
    if N < 2:
        return []
    visited = [True if i % 2 else False for i in range(N+1)]
    visited[1] = False
    visited[2] = True
    for i in range(3,int(N ** 0.5)+1):
        if visited[i] == False:
            continue
        for j in range(i+i, N+1, i):
            visited[j] = False
    
    ret = []
    for i, bool in enumerate(visited):
        if bool:
            ret.append(i)
    
    return ret

N = int(input())
prime_set = set(prime(N))

if N < 8:
    print(-1)
    exit

if N % 2:
    N -= 5
    ret = [2, 3]
else:
    N -= 4
    ret = [2, 2]

for p in prime_set:
    if N - p in prime_set:
        ret += [p, N-p]
        break

print(' '.join(str(n) for n in ret))