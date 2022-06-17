import sys
import heapq as hq

t = int(input())
for _ in range(t):
    n = int(input())
    queue_m = []
    queue_M = []
    visit = [False]*1000001
    for i in range(n):
        s, number = input().split()

        if s == 'I':
            hq.heappush(queue_m, (int(number), i))
            hq.heappush(queue_M, (-int(number), i))
            visit[i] = True
        else:
            if number == '1':
                while queue_M and not visit[queue_M[0][1]]:
                    hq.heappop(queue_M)
                if queue_M:
                    visit[queue_M[0][1]] = False
                    hq.heappop(queue_M)
            elif number == '-1':
                while queue_m and not visit[queue_m[0][1]]:
                    hq.heappop(queue_m)
                if queue_m:
                    visit[queue_m[0][1]] = False
                    hq.heappop(queue_m)

    while queue_M and not visit[queue_M[0][1]]:
        hq.heappop(queue_M)
    while queue_m and not visit[queue_m[0][1]]:
        hq.heappop(queue_m)

    if queue_M:
        print(-queue_M[0][0], queue_m[0][0])
    else:
        print('EMPTY')
