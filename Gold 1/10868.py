import sys
import math
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = min(init(node*2, start, (start+end)//2),
                         init(node*2+1, (start+end)//2+1, end))
        return tree[node]


def getMin(node, start, end, left, right, m):
    if end < left or start > right:
        return 1000000001

    if left <= start and end <= right:
        m = min(m, tree[node])
        return m

    return min(getMin(node*2, start, (start+end)//2, left, right, m), getMin(node*2+1, (start+end)//2+1, end, left, right, m))


n, m = map(int, input().rstrip().split())
l = []
tree = [0] * 2**(math.ceil(math.log2(n))+1)

for _ in range(n):
    l.append(int(input().rstrip()))

init(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(getMin(1, 0, n-1, a-1, b-1, 1000000001))
