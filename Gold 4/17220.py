import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
graph_rev = {i: [] for i in range(n)}

for i in range(m):
    a, b = map(str, input().split())
    graph[ord(a)-65].append(ord(b)-65)
    graph_rev[ord(b)-65].append(ord(a)-65)

head = []
for i in range(n):
    if graph_rev[i] == []:
        head.append(i)

arrest = list(map(str, input().split()))
arrest = arrest[1:]

for i in arrest:
    if ord(i)-65 in head:
        head.remove(ord(i)-65)

if not head:
    print(0)
else:
    for i in arrest:
        for j in range(n):
            if ord(i)-65 in graph[j]:
                graph[j].remove(ord(i)-65)

    visit = head[:]
    queue = deque(head)
    while queue:
        new = queue.pop()

        for i in graph[new]:
            if i not in visit:
                visit.append(i)
                queue.append(i)

    for i in head:
        if i in visit:
            visit.remove(i)

    print(len(visit))
