n = int(input())
a = list(map(int, input().split()))
b = [abs(a[i]) for i in range(len(a))]
d = 0

for i in range(1, max(b)):
    same = True

    for j in range(len(a)-1):
        if a[j] % i != a[j+1] % i:
            same = False

    if same:
        d = i

print(d)
