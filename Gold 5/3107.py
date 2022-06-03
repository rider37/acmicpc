s = str(input())
a = list(s.split(':'))
v = a.count('')
check = True
m = []
for i in range(len(a)):
    if a[i] != '':
        m.append('{0:0>4}'.format(a[i]))
    elif a[i] == '' and check:
        check = False
        if v == 1:
            for j in range(9-len(a)):
                m.append('0000')
        elif v == 2:
            for j in range(10-len(a)):
                m.append('0000')
print(m[0], m[1], m[2], m[3], m[4], m[5], m[6], m[7], sep=':')
