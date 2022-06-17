import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
graph_pos = [[0]*n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if matrix[r][c] == 1:
            graph[r].append(c)

for i in range(n):
    queue = dq([i])
    while queue:
        now = queue.popleft()

        for j in graph[now]:
            if graph_pos[i][j] == 0:
                graph_pos[i][j] = 1
                queue.append(j)

for i in range(n):
    print(*graph_pos[i])
