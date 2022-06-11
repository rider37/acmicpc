import sys
from collections import deque as dq
input = sys.stdin.readline


n = int(input())
m = int(input())
broken = []
if m != 0:
    broken = list(map(str, input().rstrip().split()))

channel = [i for i in range(1000001)]
channel = list(map(str, channel))

for i in broken:
    for j in range(1000001):
        if i in channel[j]:
            channel[j] = 'x'

channel = list(set(channel))
if 'x' in channel:
    channel.remove('x')

for i in range(len(channel)):
    channel[i] = abs(n-int(channel[i])) + len(channel[i])

if channel:
    print(min(min(channel), abs(n-100)))
else:
    print(abs(n-100))
