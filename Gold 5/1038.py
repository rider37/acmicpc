l = ['0']

for i in range(1, 10):
    temp = [str(i)]
    for j in range(len(l)):
        temp.append(str(i)+l[j])
    l.extend(temp)

l = list(map(int, l))
l.sort()

n = int(input())
if n >= len(l):
    print(-1)
else:
    print(l[n])
