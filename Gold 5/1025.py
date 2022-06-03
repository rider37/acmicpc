n, m = map(int, input().split())
graph = list(list(map(int, str(input()))) for _ in range(n))

max = [-1]


def hap(row, col, sum, dr, dc, j):
    drow = [0, dr, 0, -dr, dr, dr, -dr, -dr]
    dcol = [dc, 0, -dc, 0, dc, -dc, dc, -dc]

    if sum**0.5 - int(sum**0.5) == 0 and sum > max[0]:
        max[0] = sum

    if not 0 <= row+drow[j] < n:
        return
    if not 0 <= col+dcol[j] < m:
        return

    hap(row+drow[j], col+dcol[j], int(str(sum) +
        str(graph[row+drow[j]][col+dcol[j]])), dr, dc, j)


for row in range(n):
    for col in range(m):
        for dr in range(1, n+1):
            for dc in range(1, m+1):
                for j in range(8):
                    hap(row, col, graph[row][col], dr, dc, j)

print(max[0])
