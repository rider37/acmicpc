import sys
input = sys.stdin.readline

n = int(input())
meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])
time = [0]*n

m = meeting[0][1]
time[0] = 1

for i in range(1, n):
    if meeting[i][0] >= m:
        m = meeting[i][1]
        time[i] = 1

print(sum(time))
