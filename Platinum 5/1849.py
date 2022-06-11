import sys
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2, start, (start+end)//2) + \
            init(node*2+1, (start+end)//2+1, end)
        return tree[node]


def subSum(node, start, end, left, right):
    if end < left or start > right:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return subSum(node*2, start, (start+end)//2, left, right) + subSum(node*2+1, (start+end)//2+1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        update(node*2, start, (start+end)//2, index, diff)
        update(node*2+1, (start+end)//2+1, end, index, diff)


n = int(input())
tree = [0]*300000
l = [0]*n+1

a = [int(input()) for _ in range]
