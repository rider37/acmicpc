n = int(input())
sosu = [[] for _ in range(n)]
sosu[0] = [2, 3, 5, 7]

for i in range(n-1):
    for j in sosu[i]:
        for k in [1, 3, 5, 7, 9]:
            prime = True
            a = int(str(j)+str(k))
            for l in range(2, int(a**0.5)+1):
                if a % l == 0:
                    prime = False
            if prime:
                sosu[i+1].append(a)

for i in range(len(sosu[n-1])):
    print(sosu[n-1][i])
