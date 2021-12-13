import sys

N = int(sys.stdin.readline())
N_list =  list(map(int, input().split()))

minimum = 0
N_list.sort()

for index in range(N):
    for index2 in range(index+1):
        # print(index, index2)
        minimum += N_list[index2]

print(minimum)
