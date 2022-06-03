import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
    s = str(sys.stdin.readline().rstrip())
    graph.append(list(s))

graph_dis = [[[sys.maxsize]*m for _ in range(n)] for _ in range(6)]

for r in range(n):
    for c in range(m):
        if graph[r][c] == 'D':
            D = [r, c, 4, 0]
        if graph[r][c] == 'R':
            R = [r, c, 4]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

graph_dis[4][D[0]][D[1]] = 0

queue = deque([D])

while queue:
    r, c, d, cnt = queue.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        nd = d
        if graph[nr][nc] != '#':
            if d == 0:
                if i == 0:
                    nd = 4
                elif i == 1:
                    nd = 5
            elif d == 1:
                if i == 0:
                    nd = 5
                elif i == 1:
                    nd = 4
            elif d == 2:
                if i == 2:
                    nd = 4
                elif i == 3:
                    nd = 5
            elif d == 3:
                if i == 2:
                    nd = 5
                elif i == 3:
                    nd = 4
            elif d == 4:
                if i == 0:
                    nd = 1
                elif i == 1:
                    nd = 0
                elif i == 2:
                    nd = 3
                elif i == 3:
                    nd = 2
            elif d == 5:
                if i == 0:
                    nd = 0
                elif i == 1:
                    nd = 1
                elif i == 2:
                    nd = 2
                elif i == 3:
                    nd = 3

            if graph_dis[nd][nr][nc] > cnt+1:
                if [nr, nc, nd] == R:
                    graph_dis[nd][nr][nc] = cnt + 1
                elif nr == R[0] and nc == R[1]:
                    continue
                else:
                    graph_dis[nd][nr][nc] = cnt + 1
                    queue.append([nr, nc, nd, cnt+1])

if graph_dis[4][R[0]][R[1]] == sys.maxsize:
    print(-1)
else:
    print(graph_dis[4][R[0]][R[1]])
