import sys
input = sys.stdin.readline
from itertools import permutations
N = int(input())

num_list = permutations(list(map(int, input().split())))

maxNum = 0

for i in num_list:
    sum = 0
    for j in range(N-1):
        sum += abs(i[j] - i[j+1])
    maxNum = max(maxNum, sum)
print(maxNum)


