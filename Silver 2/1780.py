import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = [0]*3
k = True
for r in range(n):
    for c in range(n):
        if graph[r][c] != graph[0][0]:
            k = False

if k:
    if graph[0][0] == -1:
        cnt[0] += 1
    elif graph[0][0] == 0:
        cnt[1] += 1
    else:
        cnt[2] += 1

    for i in range(3):
        print(cnt[i])

else:
    queue = dq([[0, 0, n//3, n//3], [n//3, 0, n // 3*2, n//3], [n//3*2, 0, n, n//3],
                [0, n//3, n//3, n//3*2], [n//3, n//3, n //
                                          3*2, n//3*2], [n//3*2, n//3, n, n//3*2],
                [0, n//3*2, n//3, n], [n//3, n//3*2, n // 3*2, n], [n//3*2, n//3*2, n, n]])
    while queue:
        r_s, c_s, r_e, c_e = queue.pop()

        a = True
        b = graph[r_s][c_s]
        for r in range(r_s, r_e):
            for c in range(c_s, c_e):
                if graph[r][c] != b:
                    a = False
        if a:
            if b == -1:
                cnt[0] += 1
            elif b == 0:
                cnt[1] += 1
            else:
                cnt[2] += 1

        else:
            k = r_e - r_s
            queue.extend([[r_s, c_s, r_s+k//3, c_s+k//3], [r_s+k//3, c_s, r_s+k//3*2, c_s+k//3], [r_s+k//3*2, c_s, r_e, c_s+k//3],
                          [r_s, c_s+k//3, r_s+k//3, c_s+k//3*2], [r_s+k//3, c_s+k//3, r_s +
                                                                  k//3*2, c_s+k//3*2], [r_s+k//3*2, c_s+k//3, r_e, c_s+k//3*2],
                          [r_s, c_s+k//3*2, r_s+k//3, c_e], [r_s+k//3, c_s+k//3*2, r_s+k//3*2, c_e], [r_s+k//3*2, c_s+k//3*2, r_e, c_e]])

    for i in range(3):
        print(cnt[i])
