k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))
a.sort()
a.reverse()
b = []
for i in range(k):
    b.append(len(str(a[i])))
c = []
for i in range(k):
    c.append(a[i]//(10**(b[i]-1)))
num = [[] for i in range(9)]
for i in range(9, 0, -1):
    for j in range(k):
        if c[j] == i:
            num[i-1].append(a[j])
sum = []
overlap = True

for i in range(9):
    if len(num[i]) == 0:
        continue
    p = len(str(num[i][0]))
    for j in range(p, 0, -1):
        for l in range(len(num[i])-1):
            for h in range(len(num[i])-1):
                if int(str(num[i][h])+str(num[i][h+1])) < int(str(num[i][h+1])+str(num[i][h])):
                    tmp = num[i][h+1]
                    num[i][h+1] = num[i][h]
                    num[i][h] = tmp

for i in range(8, -1, -1):
    if len(num[i]) == 0:
        continue
    for j in range(len(num[i])):
        if num[i][j] == max(a):
            if overlap:
                for _ in range(n-k):
                    sum.append(str(num[i][j]))
                overlap = False
        sum.append(str(num[i][j]))


print(''.join(sum))
