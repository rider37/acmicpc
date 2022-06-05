import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = deque(list(str(input().rstrip())))
    d = p.count('D')
    n = int(input())
    x = str(input().rstrip())
    temp = []
    t = ''
    for i in x:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            t += i
        else:
            if t != '':
                temp.append(int(t))
            t = ''
    x = deque(temp)

    if d > n:
        print('error')
        continue
    r = False
    while p:
        k = p.popleft()
        if k == 'R':
            if r:
                r = False
            else:
                r = True
        else:
            if r:
                x.pop()
            else:
                x.popleft()
    x = list(map(str, x))
    if r:
        x.reverse()
        print('[', ','.join(x), ']', sep='')
    else:
        print('[', ','.join(x), ']', sep='')
