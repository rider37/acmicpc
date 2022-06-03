import sys

T = int(input())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    n = y-x
    if n <= 2:
        print(n)
        continue
    i = 1
    while True:
        sum = i*(i+1)
        if sum < n <= sum+i+1:
            print(2*i+1)
            break
        elif sum+i+1 < n <= sum+2*i+2:
            print(2*i+2)
            break
        i += 1
