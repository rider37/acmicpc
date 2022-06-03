from collections import deque
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n, k = map(int, sys.stdin.readline().split())
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    build_pre = [[] for _ in range(n+1)]
    dis = list(map(int, sys.stdin.readline().split()))
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        build_pre[b].append(a)
        indegree[b] += 1
    w = int(sys.stdin.readline())

    result = []
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                queue.append(i)

    for i in result:
        if len(build_pre[i]) == 0:
            continue
        elif len(build_pre[i]) != 0:
            len_max = 0
            for j in build_pre[i]:
                if dis[j-1] > len_max:
                    len_max = dis[j-1]
            dis[i-1] += len_max

    print(dis[w-1])
