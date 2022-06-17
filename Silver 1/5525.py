import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = str(input().rstrip())

p = 'I'
l = []
c = 0
for i in range(m-2):
    if i == m-3:
        if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
            p += 'OI'
        if len(p) > 2*n:
            c += (len(p)-1)//2 - n + 1
        p = 'I'
    if s[i] == 'I' and s[i+1] == 'O' and s[i+2] == 'I':
        p += 'OI'
    elif s[i] == 'O' and s[i+1] == 'I' and s[i+2] == 'O':
        continue
    else:
        if len(p) > 2*n:
            c += (len(p)-1)//2 - n + 1
        p = 'I'

print(c)
