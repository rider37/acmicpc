import sys
from collections import deque as dq
input = sys.stdin.readline

M, N, H = map(int, input().split())
graph = [[] for _ in range(H)]

for i in range(H):
    graph[i].extend([list(map(int, input().split())) for _ in range(N)])

q = True
for h in range(H):
    for r in range(N):
        if 0 in graph[h][r]:
            q = False

if q:
    print(0)

else:
    queue = dq([])
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if graph[h][r][c] == 1:
                    queue.append([h, r, c])

    dr = [0, 0, 1, -1, 0, 0]
    dc = [1, -1, 0, 0, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]

    while queue:
        h, r, c = queue.popleft()

        for i in range(6):
            nh, nr, nc = h + dh[i], r + dr[i], c + dc[i]

            if not 0 <= nh < H or not 0 <= nr < N or not 0 <= nc < M:
                continue

            if graph[nh][nr][nc] == 0:
                graph[nh][nr][nc] = graph[h][r][c] + 1
                queue.append([nh, nr, nc])
            else:
                graph[nh][nr][nc] = min(graph[h][r][c] + 1, graph[nh][nr][nc])

    a = 0
    p = True
    for h in range(H):
        for r in range(N):
            a = max(max(graph[h][r]), a)
            if 0 in graph[h][r]:
                p = False
    if p:
        print(a-1)
    else:
        print(-1)
