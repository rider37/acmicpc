import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    k = list(str(input().rstrip()))
    k = list(map(int, k))
    graph.append(k)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

dis_min = sys.maxsize

graph_dis = [[[sys.maxsize]*m for _ in range(n)] for _ in range(2)]
graph_dis[0][0][0] = 1

queue = dq([[0, 0, False]])
while queue:
    r, c, w = queue.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if not 0 <= nr < n:
            continue
        if not 0 <= nc < m:
            continue

        if not w and graph[nr][nc] == 0 and graph_dis[0][nr][nc] > graph_dis[0][r][c] + 1:
            graph_dis[0][nr][nc] = graph_dis[0][r][c] + 1
            queue.append([nr, nc, w])

        if w and graph[nr][nc] == 0 and graph_dis[1][nr][nc] > graph_dis[1][r][c] + 1:
            graph_dis[1][nr][nc] = graph_dis[1][r][c] + 1
            queue.append([nr, nc, w])

        if not w and graph[nr][nc] == 1 and graph_dis[1][nr][nc] > graph_dis[0][r][c] + 1:
            graph_dis[1][nr][nc] = graph_dis[0][r][c] + 1
            queue.append([nr, nc, True])

dis_min = min(dis_min, graph_dis[0][n-1][m-1], graph_dis[1][n-1][m-1])

if dis_min == sys.maxsize:
    print(-1)
else:
    print(dis_min)
