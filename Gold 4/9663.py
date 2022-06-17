from collections import deque as dq

n = int(input())
cnt = 0

for x in range(n):
    graph = [[1]*n for _ in range(n)]
    queue = dq([[0, x, '']])

    while queue:
        r, c, visited = queue.pop()
        if r == n-1:
            cnt += 1

        else:
            for i in range(r, n):
                if str(i) + ',' + str(c) not in visited:
                    visited += str(i) + ',' + str(c) + ' '
            for i in range(1, n):
                if r + i < n:
                    if c - i >= 0 and str(r+i) + ',' + str(c-i) not in visited:
                        visited += str(r+i) + ',' + str(c-i) + ' '
                    if c + i < n and str(r+i) + ',' + str(c+i) not in visited:
                        visited += str(r+i) + ',' + str(c+i) + ' '

            for i in range(n):
                if str(r+1) + ',' + str(i) not in visited:
                    queue.append([r+1, i, visited])

print(cnt)
