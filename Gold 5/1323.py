n, k = map(int, input().split())
m = n
count = 1

while True:
    if k % 2 == 0 and n % 2 == 1 or k % 5 == 0 and n % 10 not in [0, 5]:
        print(-1)
        break
    if count > 1 and m % k == n % k:
        print(-1)
        break
    if m % k == 0:
        print(count)
        break

    m = int(str(m % k)+str(n))
    count += 1
