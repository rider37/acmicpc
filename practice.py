import sys
input = sys.stdin.readline

N = int(input())
# distances = []
dis_cnt = [0 for _ in range(21)]

for _ in range(N):
    dis = int(input())
    # distances.append(dis)
    dis_cnt[dis] += 1

# distances.sort()

for i in range(20, 0, -1):
    dis_cnt[i-1] += dis_cnt[i]//2
    dis_cnt[i] = dis_cnt[i] % 2

print('A' if dis_cnt[0] > 0 else 'B')
