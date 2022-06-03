n, k = map(int, input().split())
s = 1
e = 3

while True:
    if k == 2**(n-1):
        print(s, e)
        break
    elif k < 2**(n-1):
        e = 6-s-e
        n -= 1
    else:
        s = 6-s-e
        k -= 2**(n-1)
        n -= 1
