import math
n = int(input())
k = int(math.log(int(n/3), 2))
a = [0]*n
a[0] = "  *"
a[1] = " * *"
a[2] = "*****"
for j in range(1, k+1):
    l = 3*(2**j)
    m = int(l/2)
    for i in range(m, l):
        a[i] = a[i-m] + " "*(l-i) + a[i-m]
    for i in range(m):
        a[i] = " "*m + a[i]
for i in range(n):
    a[i] = a[i] + " "*(n-1-i)
for i in range(n):
    print(a[i])
