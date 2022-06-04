import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(str(input().rstrip())) for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, graph[i]))
graph_dis = [[0]*m for _ in range(n)]
graph_check = [[0]*m for _ in range(n)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for _ in range(3):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph[x][y] = -1
    graph_check[x][y] += 1
    queue = deque([[x, y, 0]])
    while queue:
        r, c, d = queue.popleft()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not 0 <= nr < n:
                continue
            if not 0 <= nc < m:
                continue

            if graph[nr][nc] == 0:
                graph_dis[nr][nc] = max(graph_dis[nr][nc], d+1)
                queue.append([nr, nc, d+1])
                graph[nr][nc] = -1
                graph_check[nr][nc] += 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:
                graph[i][j] = 0

l = []
for r in range(n):
    for c in range(m):
        if graph_check[r][c] == 3:
            l.append(graph_dis[r][c])
if not l:
    print(-1)
else:
    a = min(l)
    print(a)
    print(l.count(a))
