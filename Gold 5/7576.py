import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box = []
tomato = deque([])
for _ in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))
for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            tomato.append([y, x])


dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while tomato:
    y, x = tomato.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if not 0 <= ny < n:
            continue
        if not 0 <= nx < m:
            continue

        if box[ny][nx] == 0:
            tomato.append([ny, nx])
            box[ny][nx] = box[y][x] + 1

day = 0
possible = True
for i in range(n):
    if day < max(box[i]):
        day = max(box[i])
    if 0 in box[i]:
        possible = False
        break
if possible:
    print(day-1)
else:
    print(-1)
