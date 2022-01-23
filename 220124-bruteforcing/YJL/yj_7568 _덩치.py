import sys
input = sys.stdin.readline

# 전체 사람의 수 N
N = int(input())
deongchi = []

# 사람의 몸무게와 키를 나타내는 양의 정수 x와 y
for _ in range(N):
    x, y = map(int, input().split())
    deongchi.append((x, y))


for i in deongchi:
    rank = 1
    for j in deongchi:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
