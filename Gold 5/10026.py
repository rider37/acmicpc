import sys
from collections import deque

n = int(sys.stdin.readline())

a = [i for i in range(n)]
b = []
for _ in range(n):
    b.append(list(str(sys.stdin.readline().rstrip())))
paint = dict(zip(a, b))

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

cnt = 0
for y in range(n):
    for x in range(n):
        if paint[y][x] in [0, 1, 2]:
            continue
        if paint[y][x] == 'R':
            paint[y][x] = 0
        elif paint[y][x] == 'G':
            paint[y][x] = 1
        elif paint[y][x] == 'B':
            paint[y][x] = 2
        queue = deque([[y, x]])

        while queue:
            now_y, now_x = queue.popleft()

            for i in range(4):
                ny, nx = now_y + dy[i], now_x + dx[i]

                if not 0 <= ny < n:
                    continue
                if not 0 <= nx < n:
                    continue

                if paint[now_y][now_x] == 0 and paint[ny][nx] == 'R':
                    queue.append([ny, nx])
                    paint[ny][nx] = 0
                elif paint[now_y][now_x] == 1 and paint[ny][nx] == 'G':
                    queue.append([ny, nx])
                    paint[ny][nx] = 1
                elif paint[now_y][now_x] == 2 and paint[ny][nx] == 'B':
                    queue.append([ny, nx])
                    paint[ny][nx] = 2
        cnt += 1
print(cnt)

cnt = 0
for y in range(n):
    for x in range(n):
        if paint[y][x] in ['R', 'B']:
            continue
        if paint[y][x] in [0, 1]:
            paint[y][x] = 'R'
        elif paint[y][x] == 2:
            paint[y][x] = 'B'
        queue = deque([[y, x]])

        while queue:
            now_y, now_x = queue.popleft()

            for i in range(4):
                ny, nx = now_y + dy[i], now_x + dx[i]

                if not 0 <= ny < n:
                    continue
                if not 0 <= nx < n:
                    continue

                if paint[now_y][now_x] == 'R' and paint[ny][nx] in [0, 1]:
                    queue.append([ny, nx])
                    paint[ny][nx] = 'R'
                elif paint[now_y][now_x] == 'B' and paint[ny][nx] == 2:
                    queue.append([ny, nx])
                    paint[ny][nx] = 'B'
        cnt += 1
print(cnt)
