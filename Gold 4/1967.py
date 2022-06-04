import sys
import heapq
input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
else:
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}

    for _ in range(n-1):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    dis = {i: sys.maxsize for i in graph}
    dis[1] = 0

    queue = []
    heapq.heappush(queue, [dis[1], 1])
    while queue:
        cdis, c = heapq.heappop(queue)
        if dis[c] < cdis:
            continue

        for new, new_dis in graph[c].items():
            temp = cdis + new_dis

            if temp < dis[new]:
                dis[new] = temp
                heapq.heappush(queue, [temp, new])

    a = 0
    s = 0
    for i in dis:
        if dis[i] > a:
            a = dis[i]
            s = i

    dis = {i: sys.maxsize for i in graph}
    dis[s] = 0

    queue = []
    heapq.heappush(queue, [dis[s], s])
    while queue:
        cdis, c = heapq.heappop(queue)
        if dis[c] < cdis:
            continue

        for new, new_dis in graph[c].items():
            temp = cdis + new_dis

            if temp < dis[new]:
                dis[new] = temp
                heapq.heappush(queue, [temp, new])

    b = 0
    for i in dis:
        if dis[i] > b:
            b = dis[i]

    print(b)
