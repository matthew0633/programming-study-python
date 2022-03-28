import sys
input = sys.stdin.readline

T = int(input())

def sum(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    elif N == 3:
        return 4
    else:
        return sum(N-1) + sum(N-2) + sum(N-3)

for i in range(T):
    num = int(input())
    print(sum(num))