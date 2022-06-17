import sys
input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())
dp_max, dp_min = [a, b, c], [a, b, c]

for _ in range(n-1):
    a, b, c = map(int, input().split())

    for i in range(3):
        if i == 0:
            dp_min_0 = a + min(dp_min[1], dp_min[0])
            dp_max_0 = a + max(dp_max[1], dp_max[0])
        elif i == 2:
            dp_min_2 = c + min(dp_min[1], dp_min[2])
            dp_max_2 = c + max(dp_max[1], dp_max[2])
        else:
            dp_min_1 = b + min(dp_min[1], dp_min[2], dp_min[0])
            dp_max_1 = b + max(dp_max[1], dp_max[2], dp_max[0])

    dp_min = [dp_min_0, dp_min_1, dp_min_2]
    dp_max = [dp_max_0, dp_max_1, dp_max_2]

print(max(dp_max), min(dp_min))
