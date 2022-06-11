import sys
from collections import deque as dq
input = sys.stdin.readline

n, k = map(int, input().split())
if n == k:
    print(0)
    print(1)
else:
    m = max(n+1, k+1)
    graph = [[0, sys.maxsize] for _ in range(m+1)]
    graph[n] = [0, 0]
    queue = dq([n])
    while queue:
        current = queue.popleft()

        if 2*current <= m:
            if graph[2*current][1] >= graph[current][1] + 1:
                graph[2*current][1] = graph[current][1] + 1
                graph[2*current][0] += 1
                queue.append(2*current)
        if 0 <= current - 1 <= m:
            if graph[current-1][1] >= graph[current][1] + 1:
                graph[current-1][1] = graph[current][1] + 1
                graph[current-1][0] += 1
                queue.append(current-1)
        if 0 <= current + 1 <= m:
            if graph[current+1][1] >= graph[current][1] + 1:
                graph[current+1][1] = graph[current][1] + 1
                graph[current+1][0] += 1
                queue.append(current+1)

    print(graph[k][1])
    print(graph[k][0])
