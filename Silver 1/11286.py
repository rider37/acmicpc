import heapq
import sys

n = int(sys.stdin.readline())
p = []
m = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(p, x)
    elif x < 0:
        heapq.heappush(m, -x)
    elif x == 0:
        if not p and not m:
            print(0)
        elif not p and m:
            print(-heapq.heappop(m))
        elif p and not m:
            print(heapq.heappop(p))
        else:
            if p[0] < m[0]:
                print(heapq.heappop(p))
            else:
                print(-heapq.heappop(m))
