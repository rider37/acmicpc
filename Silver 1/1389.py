import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(101)]
graph_dis = [[sys.maxsize]*(101) for _ in range(101)]
p = []
for _ in range(m):
    a, b = map(int, input().split())
    if b not in graph[a]:
        graph[a].append(b)
    if a not in graph[b]:
        graph[b].append(a)
    p.append(a)
    p.append(b)
p = list(set(p))

for i in range(1, 101):
    graph_dis[i][i] = 0
    graph_dis[i][0] = 0
    queue = dq([i])
    while queue:
        now = queue.popleft()

        for j in graph[now]:
            if graph_dis[i][j] > graph_dis[i][now] + 1:
                graph_dis[i][j] = graph_dis[i][now] + 1
                queue.append(j)

for i in p:
    for j in range(1, 101):
        if graph_dis[i][j] == sys.maxsize:
            graph_dis[i][j] = 0

disSum = [0]*101
for i in range(1, 101):
    disSum[i] = sum(graph_dis[i])
a = 1
b = sys.maxsize
for i in range(1, 101):
    if b > disSum[i]:
        a = i
        b = disSum[i]

print(a)
