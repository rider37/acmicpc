p = []
for _ in range(3):
    p.append(list(map(int, input().split())))


def side(p1, p2, p3):
    return (p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])


if p[1][1] - p[0][1] > 0:
    dir = 'up'
elif p[1][1] - p[0][1] < 0:
    dir = 'down'
else:
    if p[1][0] - p[0][0] > 0:
        dir = 'left'
    else:
        dir = 'right'

a = side(p[0], p[1], p[2])

if a == 0:
    print(0)
elif dir == 'left':
    if p[2][1] > p[1][1]:
        print(1)
    else:
        print(-1)
elif dir == 'right':
    if p[2][1] > p[1][1]:
        print(1)
    else:
        print(-1)
elif dir == 'up':
    if a > 0:
        print(1)
    else:
        print(-1)
elif dir == 'down':
    if a > 0:
        print(1)
    else:
        print(-1)
