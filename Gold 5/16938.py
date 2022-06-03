import copy

n, l, r, x = map(int, input().split())
a = list(map(int, input().split()))


result = []


def recur(subset, i, arr):
    if i == len(arr):
        result.append(copy.copy(subset))
        return

    else:
        subset.append(arr[i])
        i += 1
        recur(subset, i, arr)
        subset.pop()
        recur(subset, i, arr)


recur([], 0, a)
case = []
case_l = []
case_r = []
case_x = []
for i in range(len(result)):
    if len(result[i]) > 1:
        case.append(result[i])
for i in range(len(case)):
    if sum(case[i]) >= l:
        case_l.append(case[i])
for i in range(len(case_l)):
    if sum(case_l[i]) <= r:
        case_r.append(case_l[i])
for i in range(len(case_r)):
    if max(case_r[i]) - min(case_r[i]) >= x:
        case_x.append(case_r[i])
print(len(case_x))
