import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
h = [0]*257

for r in range(n):
    for c in range(m):
        h[graph[r][c]] += 1

ans = [sys.maxsize, 0]
for i in range(257):
    t = 0
    k = 0

    for j in range(257):
        if j > i:
            t += h[j]*2*(j-i)
            k += h[j]*(j-i)
        elif j < i:
            t += h[j]*(i-j)
            k -= h[j]*(i-j)

    if b+k < 0:
        continue
    if t <= ans[0]:
        ans = [t, i]

print(*ans)
