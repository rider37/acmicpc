import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

dr = [0, 0, 1, -1, 1, 1, -1, -1]
dc = [1, -1, 0, 0, 1, -1, 1, -1]

graph = [[5]*n for _ in range(n)]
s2d2 = [list(map(int, input().split())) for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
summer = [[0]*n for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x-1][y-1].append(z)

for _ in range(k):
    for r in range(n):
        for c in range(n):
            dead = 0
            temp = []
            if tree[r][c]:
                for _ in range(len(tree[r][c])):
                    age = tree[r][c].popleft()
                    if age <= graph[r][c]:
                        temp.append(age+1)
                        graph[r][c] -= age
                    else:
                        dead += age//2
            graph[r][c] += dead
            tree[r][c].extend(temp)

    for r in range(n):
        for c in range(n):
            for a in tree[r][c]:
                if a % 5 == 0:
                    for i in range(8):
                        if not 0 <= r + dr[i] < n or not 0 <= c + dc[i] < n:
                            continue
                        tree[r+dr[i]][c+dc[i]].appendleft(1)

    for r in range(n):
        for c in range(n):
            graph[r][c] += s2d2[r][c]

cnt = 0
for r in range(n):
    for c in range(n):
        cnt += len(tree[r][c])
print(cnt)
