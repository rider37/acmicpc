n = int(input())

if n < 10:
    print(0)
else:
    l = [[0]*10 for i in range(9)]
    for i in range(1, 10):
        l[i-1][i] = 1
    print(l)
