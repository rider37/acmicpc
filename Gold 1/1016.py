n, m = map(int, input().split())
squeare_check = [1 for _ in range(m-n+1)]
for i in range(2, int(m**0.5)+1):
    k = i**2
    s = (n//k)*k
    while s <= m:
        if n <= s <= m:
            squeare_check[s-n] = 0
        s += k
print(sum(squeare_check))
