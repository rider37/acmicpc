import sys
from collections import deque as dq
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v = int(input())
e = int(input())
parent = [i for i in range(v+1)]

graph = []
for _ in range(e):
    a, b, c = map(int, input().split())
    graph.append([c, a, b])
graph.sort()
graph = dq(graph)

cnt = 0
dis = 0

while cnt < v-1:
    c, a, b = graph.popleft()
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        dis += c

print(dis)
