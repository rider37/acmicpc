import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = dq([])
for r in range(n):
    for c in range(n):
        if graph[r][c] == 9:
            queue.append([r, c, 2, 0])
            graph[r][c] = 0

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

dis_sum = 0
while queue:
    r, c, s, t = queue.popleft()
    if s == t:
        s += 1
        t = 0

    possible = []
    fish = dq([[r, c]])
    graph_dis = [[sys.maxsize]*n for _ in range(n)]
    graph_dis[r][c] = 0

    while fish:
        y, x = fish.popleft()

        for i in range(4):
            ny, nx = y + dr[i], x + dc[i]

            if not 0 <= ny < n or not 0 <= nx < n:
                continue

            if 0 < graph[ny][nx] < s and graph_dis[ny][nx] > graph_dis[y][x] + 1:
                graph_dis[ny][nx] = graph_dis[y][x] + 1
                possible.append([graph_dis[ny][nx], ny, nx])
            elif graph[ny][nx] == s or graph[ny][nx] == 0:
                if graph_dis[ny][nx] > graph_dis[y][x] + 1:
                    graph_dis[ny][nx] = graph_dis[y][x] + 1
                    fish.append([ny, nx])

    if possible:
        possible.sort(key=lambda x: x[2])
        possible.sort(key=lambda x: x[1])
        possible.sort(key=lambda x: x[0])

        dis_sum += possible[0][0]
        queue.append([possible[0][1], possible[0][2], s, t+1])
        graph[possible[0][1]][possible[0][2]] = 0

print(dis_sum)
