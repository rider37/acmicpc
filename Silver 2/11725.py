import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parent = [0]*(n+1)
queue = deque([1])
while queue:
    node = queue.popleft()

    for i in graph[node]:
        graph[i].remove(node)
        parent[i] = node

    queue.extend(graph[node])

for i in range(2, n+1):
    print(parent[i])
