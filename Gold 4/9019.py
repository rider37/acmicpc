import sys
from collections import deque as dq
input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())

    graph = ['']*10001
    visited = [False]*10001
    visited[a] = True
    queue = dq([a])
    while queue:
        n = queue.popleft()

        for i in ['D', 'S', 'L', 'R']:
            if i == 'D' and not visited[n*2 % 10000]:
                queue.append(n*2 % 10000)
                graph[n*2 % 10000] = graph[n] + i
                visited[n*2 % 10000] = True
            elif i == 'S':
                if n == 0 and not visited[9999]:
                    queue.append(9999)
                    graph[9999] = graph[n] + i
                    visited[9999] = True
                elif n != 0 and not visited[n-1]:
                    queue.append(n-1)
                    graph[n-1] = graph[n] + i
                    visited[n-1] = True
            elif i == 'L' and not visited[(n % 1000)*10+(n//1000)]:
                queue.append((n % 1000)*10+(n//1000))
                graph[(n % 1000)*10+(n//1000)] = graph[n] + i
                visited[(n % 1000)*10+(n//1000)] = True
            elif i == 'R' and not visited[(n//10)+(n % 10)*1000]:
                queue.append((n//10)+(n % 10)*1000)
                graph[(n//10)+(n % 10)*1000] = graph[n] + i
                visited[(n//10)+(n % 10)*1000] = True

        if visited[b]:
            print(graph[b])
            break
