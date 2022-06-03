import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = list(list(map(int, input().split())) for _ in range(n))

drow = [0, 0, 1, -1]
dcol = [1, -1, 0, 0]

cnt = 0
a = 0
while True:
    s = 0
    for i in range(n):
        s += sum(graph[i])
    if s == 0:
        print(cnt)
        print(a)
        break
    a = s

    c_empty = []

    for y in range(n):
        for x in range(m):
            if graph[y][x] != 0:
                continue
            empty = []
            queue = deque([[y, x]])
            graph[y][x] = -1
            while queue:
                now_row, now_col = queue.popleft()
                empty.append([now_row, now_col])
                for i in range(4):
                    next_row, next_col = now_row + drow[i], now_col + dcol[i]

                    if not 0 <= next_row < n:
                        continue
                    if not 0 <= next_col < m:
                        continue

                    if graph[next_row][next_col] == 0:
                        graph[next_row][next_col] = -1
                        queue.append([next_row, next_col])
            ch = True
            for i in range(len(empty)):
                if 0 in empty[i]:
                    ch = False
                    break
            if ch:
                c_empty.extend(empty)

    for y in range(n):
        if -1 not in graph[y]:
            continue
        for x in range(m):
            if graph[y][x] == -1:
                graph[y][x] = 0

    for y in range(n):
        for x in range(m):
            if graph[y][x] != 1:
                continue
            check = []
            ch = True
            for i in range(4):
                if not 0 <= y+drow[i] < n:
                    continue
                if not 0 <= x+dcol[i] < m:
                    continue
                if graph[y+drow[i]][x+dcol[i]] == 0:
                    check.append([y+drow[i], x+dcol[i]])

            for i in range(len(check)):
                if check[i] not in c_empty:
                    ch = False
            if not ch:
                graph[y][x] = 2

    for y in range(n):
        if 2 not in graph[y]:
            continue
        for x in range(m):
            if graph[y][x] == 2:
                graph[y][x] = 0
    cnt += 1
