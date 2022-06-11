import sys
import math
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) * \
            init(node*2+1, (start+end)//2+1, end) % 1000000007
        return tree[node]


def subPro(node, start, end, left, right):
    if end < left or start > right:
        return 1

    if left <= start and end <= right:
        return tree[node]

    return subPro(node*2, start, (start+end)//2, left, right) * subPro(node*2+1, (start+end)//2+1, end, left, right)


def update(node, start, end, index, new, old):
    if index < start or index > end:
        return

    tree[node] //= old
    tree[node] *= new % 1000000007

    if start != end:
        update(node*2, start, (start+end)//2, index, new, old)
        update(node*2+1, (start+end)//2+1, end, index, new, old)


n, m, k = map(int, input().rstrip().split())

l = []
tree = [0] * 2**(math.ceil(math.log2(n))+1)

for _ in range(n):
    l.append(int(input().rstrip()))

init(1, 0, n-1)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        if l[b-1] == 0:
            l[b-1] = c
            init(1, 0, n-1)
        else:
            new = c
            old = l[b-1]
            l[b-1] = c
            update(1, 0, n-1, b-1, new, old)
    else:
        print(subPro(1, 0, n-1, b-1, c-1) % 1000000007)
