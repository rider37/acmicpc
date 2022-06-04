l_1 = list(str(input()))
l_2 = list(str(input()))

dp = [[0]*(len(l_2)+1) for _ in range(len(l_1)+1)]

for i in range(len(l_1)):
    for j in range(len(l_2)):
        if l_1[i] == l_2[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[-1][-1])
