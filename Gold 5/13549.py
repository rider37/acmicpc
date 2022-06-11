import sys
from collections import deque as dq
input = sys.stdin.readline

n, k = map(int, input().split())
m = max(n+1, k+1)
graph = [sys.maxsize]*(m+1)
graph[n] = 0

queue = dq([n])
while queue:
    current = queue.popleft()

    if 2*current <= m and graph[2*current] > graph[current]:
        graph[2*current] = graph[current]
        queue.append(2*current)
    if 0 <= current - 1 <= m and graph[current-1] > graph[current] + 1:
        graph[current-1] = graph[current] + 1
        queue.append(current-1)
    if 0 <= current + 1 <= m and graph[current+1] > graph[current] + 1:
        graph[current+1] = graph[current] + 1
        queue.append(current+1)

print(graph[k])
