import sys
input = sys.stdin.readline

# https://pacific-ocean.tistory.com/199

N = int(input())
# 상담을 완료하는데 걸리는 기간 T
# 상담을 했을 때 받을 수 있는 금액 P
t = []
p = []
leave = []

for _ in range(N):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    leave.append(b)
leave.append(0)
# print(leave)

for i in range(N - 1, -1, -1):
    if t[i] + i > N:
        leave[i] = leave[i + 1]
    else:
        leave[i] = max(leave[i + 1], leave[i] + leave[i + t[i]])
        # (1)[현재 일을 맡았을 때 들어오는 보상 + 현재 일을 끝낸 다음날에 쌓여있는 보상]
        # (2)일을 맡지 않을 경우 보상
        # 둘을 비교하여 큰 값을 받아주면 된다. 
print(leave[0])