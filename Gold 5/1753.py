import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())
graph = {}
for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):
    u, v, w = map(int, input().split())
    if v in graph[u]:
        graph[u][v] = min(graph[u][v], w)
    else:
        graph[u][v] = w

dis = {i: sys.maxsize for i in graph}
dis[k] = 0

queue = []
heapq.heappush(queue, [dis[k], k])
while queue:
    cdis, c = heapq.heappop(queue)
    if dis[c] < cdis:
        continue

    for new, new_dis in graph[c].items():
        temp = cdis + new_dis

        if temp < dis[new]:
            dis[new] = temp
            heapq.heappush(queue, [temp, new])

for i in dis:
    if dis[i] != sys.maxsize:
        print(dis[i])
    else:
        print('INF')
