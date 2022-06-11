import sys
import math
input = sys.stdin.readline


def init_min(node, start, end):
    if start == end:
        tree_min[node] = l[start]
        return tree_min[node]
    else:
        tree_min[node] = min(init_min(node*2, start, (start+end)//2),
                             init_min(node*2+1, (start+end)//2+1, end))
        return tree_min[node]


def init_max(node, start, end):
    if start == end:
        tree_max[node] = l[start]
        return tree_max[node]
    else:
        tree_max[node] = max(init_max(node*2, start, (start+end)//2),
                             init_max(node*2+1, (start+end)//2+1, end))
        return tree_max[node]


def getMin(node, start, end, left, right, m):
    if end < left or start > right:
        return 1000000001

    if left <= start and end <= right:
        m = min(m, tree_min[node])
        return m

    return min(getMin(node*2, start, (start+end)//2, left, right, m), getMin(node*2+1, (start+end)//2+1, end, left, right, m))


def getMax(node, start, end, left, right, m):
    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        m = max(m, tree_max[node])
        return m

    return max(getMax(node*2, start, (start+end)//2, left, right, m), getMax(node*2+1, (start+end)//2+1, end, left, right, m))


n, m = map(int, input().rstrip().split())
l = []
tree_min = [0] * 2**(math.ceil(math.log2(n))+1)
tree_max = [0] * 2**(math.ceil(math.log2(n))+1)

for _ in range(n):
    l.append(int(input().rstrip()))

init_min(1, 0, n-1)
init_max(1, 0, n-1)

for _ in range(m):
    a, b = map(int, input().split())
    print(getMin(1, 0, n-1, a-1, b-1, 1000000001),
          getMax(1, 0, n-1, a-1, b-1, 0))
