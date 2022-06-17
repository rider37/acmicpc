import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {}
for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        graph[a][b] = min(graph[a][b], c)
    else:
        graph[a][b] = c

graph_dis = [[sys.maxsize]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph_dis[i][i] = 0

    queue = dq([i])
    while queue:
        now = queue.popleft()

        for j in graph[now]:
            if graph_dis[i][j] > graph_dis[i][now] + graph[now][j]:
                graph_dis[i][j] = graph_dis[i][now] + graph[now][j]
                queue.append(j)

    for j in range(1, n+1):
        if graph_dis[i][j] == sys.maxsize:
            graph_dis[i][j] = 0
    print(*graph_dis[i][1:])
