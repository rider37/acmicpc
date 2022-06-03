n = int(input())
p = list(map(int, input().split()))
s = list(map(int, input().split()))

card = [i for i in range(n)]
card_fir = [i for i in range(n)]
tmp = []
cor = list([] for _ in range(3))
shf = list([] for _ in range(3))
shf_fir = list([] for _ in range(3))
for i in range(n):
    shf_fir[i % 3].append(card[i])
for i in range(n):
    cor[p[i]].append(i)

count = 0

while True:
    for i in range(n):
        shf[i % 3].append(card[i])
    for i in range(3):
        shf[i].sort()

    if shf == cor:
        print(count)
        break
    if count > 0 and shf == shf_fir and card == card_fir:
        print(-1)
        break

    for i in range(3):
        shf[i].clear()
    for i in range(n):
        tmp.append(card[s.index(i)])
    card.clear()
    for _ in range(n):
        card.append(tmp.pop(0))

    count += 1
