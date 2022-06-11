import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
graph = [list(str(input().rstrip())) for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, graph[i]))


queue = dq([[0, 0, n, n]])
while queue:
    r_s, c_s, r_e, c_e = queue.pop()
    d = r_e - r_s

    s = 0
    for r in range(r_s, r_e):
        for c in range(c_s, c_e):
            s += graph[r][c]

    if s == 0 or s == d**2:
        print(graph[r_s][r_s], end='')
    else:
        d //= 2
        queue.extend([[r_s+d, c_s+d, r_e, c_e], [r_s+d, c_s, r_e, c_s+d],
                     [r_s, c_s+d, r_s+d, c_e], [r_s, c_s, r_s+d, c_s+d]])
