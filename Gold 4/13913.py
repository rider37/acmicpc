from collections import deque as dq

n, k = map(int, input().split())
m = max(n+1, k+1)
graph = ['']*(100001)

if k < n:
    print(n-k)
    print(*[i for i in range(n, k-1, -1)])
elif k == n:
    print(0)
    print(k)
else:
    queue = dq([n])
    while graph[k] == '':
        now = queue.popleft()
        if k < now:
            if 0 <= now - 1 <= m:
                if graph[now-1] == '' or len(graph[now-1]) > len(graph[now])+2:
                    graph[now-1] = graph[now] + '0'
                    queue.append(now-1)
        else:
            if 2*now <= 100001 and now != 0:
                if graph[2*now] == '' or len(graph[2*now]) > len(graph[now])+2:
                    graph[2*now] = graph[now] + '2'
                    queue.append(2*now)
            if 0 <= now - 1:
                if graph[now-1] == '' or len(graph[now-1]) > len(graph[now])+2:
                    graph[now-1] = graph[now] + '0'
                    queue.append(now-1)
            if now + 1 <= 100001:
                if graph[now+1] == '' or len(graph[now+1]) > len(graph[now])+2:
                    graph[now+1] = graph[now] + '1'
                    queue.append(now+1)
    print(len(graph[k]))
    route = [n]
    c = n
    for i in range(len(graph[k])):
        if graph[k][i] == '2':
            c *= 2
        elif graph[k][i] == '0':
            c -= 1
        else:
            c += 1
        route.append(c)
    print(*route)
