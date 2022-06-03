x_s, y_s = map(int, input().split())
x_e, y_e, dx, dy = map(int, input().split())

if dx != 0 and dy != 0:
    for i in range(1, min(abs(dx)+1, abs(dy)+1)):
        if abs(dx) % i == 0 and abs(dy) % i == 0:
            gcf = i
    dx, dy = dx//gcf, dy//gcf
if dx == 0:
    if dy > 0:
        dy = 1
    elif dy < 0:
        dy = -1

if dy == 0:
    if dx > 0:
        dx = 1
    elif dx < 0:
        dx = -1


while True:
    dis = (x_s-x_e)**2 + (y_s-y_e)**2
    dis_next = (x_s-x_e-dx)**2 + (y_s-y_e-dy)**2

    if dis_next > dis:
        print(x_e, y_e)
        break

    x_e += dx
    y_e += dy
