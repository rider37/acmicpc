import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while True:
    k = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                k = True
    if not k:
        break

    queue = deque([[0, 0]])
    graph[0][0] = -1
    cheese = []

    while queue:
        r, c = queue.pop()

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not 0 <= nr < n:
                continue
            if not 0 <= nc < m:
                continue

            if graph[nr][nc] == 0:
                graph[nr][nc] = -1
                queue.append([nr, nc])
            if graph[nr][nc] == 1:
                cheese.append([nr, nc])

    while cheese:
        r, c = cheese.pop()
        v = 0

        for i in range(4):
            if graph[r+dr[i]][c+dc[i]] == -1:
                v += 1

        if v > 1:
            graph[r][c] = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] == -1:
                graph[i][j] = 0

    cnt += 1

print(cnt)
