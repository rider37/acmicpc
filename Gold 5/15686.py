import sys
from itertools import combinations, permutations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for r in range(n):
    for c in range(n):
        if graph[r][c] == 1:
            house.append([r, c])
        elif graph[r][c] == 2:
            chicken.append([r, c])

l_c, l_h = len(chicken), len(house)

chicken_dis = [[0]*(l_c) for _ in range(l_h)]
for i in range(l_h):
    for j in range(l_c):
        chicken_dis[i][j] = abs(house[i][0] - chicken[j][0]) + \
            abs(house[i][1] - chicken[j][1])

c_m = list(combinations([i for i in range(l_c)], m))

min_dis = sys.maxsize
for i in range(len(c_m)):
    dis = 0
    for j in range(l_h):
        d = 2500
        for k in c_m[i]:
            d = min(d, chicken_dis[j][k])
        dis += d
    min_dis = min(min_dis, dis)
print(min_dis)
