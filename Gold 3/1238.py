import sys
import heapq
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = {}
for i in range(1, n+1):
    graph[i] = {}

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s][e] = t

go = [0]*(n+1)
back = []

for i in range(1, n+1):
    dis = {k: sys.maxsize for k in graph}
    dis[i] = 0

    queue = []
    heapq.heappush(queue, [dis[i], i])
    while queue:
        cdis, c = heapq.heappop(queue)
        if dis[c] < cdis:
            continue

        for new, new_dis in graph[c].items():
            temp = cdis + new_dis

            if temp < dis[new]:
                dis[new] = temp
                heapq.heappush(queue, [temp, new])

    if i == x:
        back = dis
    else:
        go[i] = dis[x]

time = [0]*(n+1)
for i in range(1, n+1):
    time[i] = go[i] + back[i]
print(max(time))
