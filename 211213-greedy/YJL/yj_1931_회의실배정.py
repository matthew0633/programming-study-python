# 출처: https://suri78.tistory.com/26 [공부노트]
import sys

N = int(sys.stdin.readline())
count = temp = 0

time = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
for s, e in time:
    if s >= temp:
        count += 1
        temp = e
print(count)

# print('------------------')

# time = []
# for _ in range(N):
#     start, end = map(int, sys.stdin.readline().split())
#     time.append((start, end))
# sorted(time)

# print(time)
# # [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
# print(time[0])
# # (1, 4)
# print('------------------')