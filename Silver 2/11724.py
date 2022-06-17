import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visit = []
for i in range(1, n+1):
    if i in visit:
        continue
    queue = dq([i])
    while queue:
        now = queue.popleft()

        for j in range(len(graph[now])):
            k = graph[now].pop()
            graph[k].remove(now)
            visit.append(k)
            queue.append(k)

    cnt += 1

print(cnt)
