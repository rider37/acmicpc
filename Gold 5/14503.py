import sys
input = sys.stdin.readline

n, m = map(int, input().split())
robot = [list(map(int, input().split())) + [1]]
graph = [list(map(int, input().split())) for _ in range(n)]
graph[robot[0][0]][robot[0][1]] = 2

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
br = [1, 0, -1, 0]
bc = [0, -1, 0, 1]

while robot:
    r, c, d, cnt = robot.pop()

    for _ in range(4):
        d -= 1
        if d < 0:
            d = 3
        if graph[r+dr[d]][c+dc[d]] == 0:
            robot.append([r+dr[d], c+dc[d], d, cnt+1])
            graph[r+dr[d]][c+dc[d]] = 2
            break

    if not robot:
        if graph[r+br[d]][c+bc[d]] == 1:
            print(cnt)
            break
        robot.append([r+br[d], c+bc[d], d, cnt])

if robot:
    print(robot[0][3])
