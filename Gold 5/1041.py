import sys

n = int(input())
dice = list(map(int, sys.stdin.readline().split()))

if n == 1:
    print(sum(dice)-max(dice))
else:
    sum_min = n**3*max(dice)*3
    for i in [0, 5]:
        for j in [2, 3]:
            for k in [1, 4]:
                dice_pos = [dice[i], dice[j], dice[k]]
                dice_pos.sort()
                face_st = n**2*min(dice_pos)
                face_nd = face_st + 2*n*(dice_pos[1]-dice_pos[0])
                face_rd = face_nd + 2 * \
                    (n-2)*(dice_pos[1]-dice_pos[0]) + \
                    4*(dice_pos[2]-dice_pos[1])
                if 2*(face_st+face_nd)+face_rd < sum_min:
                    sum_min = 2*(face_st+face_nd)+face_rd
    print(sum_min)
