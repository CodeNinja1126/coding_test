'''
백준 1069번 집으로
'''
X, Y, D, T = map(int, input().split())

cand1 = (X**2 + Y**2) ** 0.5
dist = cand1
cand2 = 0

while True:
    if dist < D:
        break
    dist -= D
    cand2 += T

cand3 = T + (D - dist) + cand2
cand4 = cand2 + T if cand2 > 0 else 2*T
cand2 += dist

print(min(cand3, cand2, cand1, cand4))