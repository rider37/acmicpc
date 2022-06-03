from collections import deque

N, e, w, s, n = map(int, input().split())
a = [e/100, w/100, s/100, n/100]

start = str(N) + ', ' + str(N)
queue = deque([[100, 100, 1, 0, start]])

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

s = 0

while queue:
    r, c, p, cnt, visit = queue.pop()

    for i in range(4):
        if a[i] == 0:
            continue
        nr, nc = r + dr[i], c + dc[i]

        nrc = str(nr) + ',' + str(nc)

        if visit.find(nrc) == -1:
            if cnt == N:
                s += p*a[i]
            else:
                queue.append([nr, nc, p*a[i], cnt+1, visit+' '+nrc])
print(s)
