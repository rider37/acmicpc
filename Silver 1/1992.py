import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
graph = [list(str(input().rstrip())) for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, graph[i]))


def func(r_s, c_s, r_e, c_e):
    d = r_e - r_s
    s = 0
    for r in range(r_s, r_e):
        for c in range(c_s, c_e):
            s += graph[r][c]

    if s == 0 or s == d**2:
        if s == 0:
            print(0, end='')
        else:
            print(1, end='')
    else:
        d //= 2
        print('(', end='')
        func(r_s, c_s, r_s+d, c_s+d)
        func(r_s, c_s+d, r_s+d, c_e)
        func(r_s+d, c_s, r_e, c_s+d)
        func(r_s+d, c_s+d, r_e, c_e)
        print(')', end='')


func(0, 0, n, n)
