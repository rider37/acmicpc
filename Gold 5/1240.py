n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graph_dis = [[[] for _ in range(n+1)] for _ in range(n+1)]

for _ in range(n-1):
    l, u, d = map(int, input().split())
    graph[l].append(u)
    graph[u].append(l)
    graph_dis[l][u].append(d)
    graph_dis[u][l].append(d)


visit = []


def dfs(now, end, dis):
    if now == end:
        print(dis)
        return

    for i in graph[now]:
        if i in visit:
            continue
        visit.append(i)
        dfs(i, end, dis+graph_dis[now][i][0])
        visit.pop()


for _ in range(m):
    start, end = map(int, input().split())
    visit.append(start)
    dfs(start, end, 0)
    visit.clear()
