import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
graph = [list(str(input().rstrip())) for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, graph[i]))

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

estate = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            queue = dq([[r, c]])
            graph[r][c] = 0
            cnt = 1
            while queue:
                cr, cc = queue.popleft()

                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]

                    if not 0 <= nr < n:
                        continue
                    if not 0 <= nc < n:
                        continue

                    if graph[nr][nc] == 1:
                        graph[nr][nc] = 0
                        queue.append([nr, nc])
                        cnt += 1
            estate.append(cnt)

estate.sort()
print(len(estate))
for i in estate:
    print(i)
