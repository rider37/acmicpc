import sys
input = sys.stdin.readline

n, k = map(int, input().split())
l = [[0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(k+1)]

for i in range(1, k+1):
    for j in range(1, n+1):
        if l[j][0] > i:
            dp[i][j] = dp[i][j-1]
        if l[j][0] <= i:
            dp[i][j] = max(dp[i][j-1], dp[i-l[j][0]][j-1] + l[j][1])

m = 0
for i in range(1, k+1):
    m = max(m, max(dp[i]))
print(m)
