import sys
from collections import deque as dq
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
paper = [0, 0]


def func(r_s, c_s, r_e, c_e):
    d = r_e - r_s
    s = 0
    for r in range(r_s, r_e):
        for c in range(c_s, c_e):
            s += graph[r][c]

    if s == 0 or s == d**2:
        if s == 0:
            paper[0] += 1
        else:
            paper[1] += 1
    else:
        d //= 2
        func(r_s, c_s, r_s+d, c_s+d)
        func(r_s, c_s+d, r_s+d, c_e)
        func(r_s+d, c_s, r_e, c_s+d)
        func(r_s+d, c_s+d, r_e, c_e)


func(0, 0, n, n)
print(paper[0])
print(paper[1])
