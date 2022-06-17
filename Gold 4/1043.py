import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())
pt = list(map(int, input().split()))
pt = pt[1:]
party = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n+1)]
for i in range(m):
    for j in range(1, party[i][0]):
        for k in range(j+1, party[i][0]+1):
            if party[i][k] not in graph[party[i][j]]:
                graph[party[i][k]].append(party[i][j])
                graph[party[i][j]].append(party[i][k])

queue = dq(pt)
while queue:
    now = queue.popleft()

    for i in graph[now]:
        if i not in pt:
            pt.append(i)
            queue.append(i)

cnt = 0
for i in range(m):
    p = True

    for j in party[i][1:]:
        if j in pt:
            p = False
            break

    if p:
        cnt += 1

print(cnt)
