import sys
from collections import deque as dq
input = sys.stdin.readline

n, m = map(int, input().split())
radder = [0]*101

for _ in range(n+m):
    x, y = map(int, input().split())
    radder[x] = y

visited = [False]*101
visited[1] = True
cnt = [0]*101

queue = dq([1])
while not visited[100]:
    now = queue.popleft()

    for i in range(1, 7):
        if not 0 < now + i < 101:
            continue
        if visited[now+i]:
            continue

        if radder[now+i] != 0 and not visited[radder[now+i]]:
            visited[now+i] = True
            visited[radder[now+i]] = True
            cnt[now+i] = cnt[now] + 1
            cnt[radder[now+i]] = cnt[now] + 1
            queue.append(radder[now+i])
        elif radder[now+i] == 0:
            visited[now+i] = True
            cnt[now+i] = cnt[now] + 1
            queue.append(now+i)

print(cnt[100])
