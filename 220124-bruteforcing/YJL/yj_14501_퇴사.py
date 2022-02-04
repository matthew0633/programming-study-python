import sys
input = sys.stdin.readline

N = int(input())

timeTable = [list(map(int,sys.stdin.readline().split())) for i in range(N)]

dp = [0 for _ in range(N+1)]

# 상담을 완료하는데 걸리는 기간 : timeTable[i][0] 
# 상담을 했을 때 받을 수 있는 금액 : timeTable[i][1]
for i in range(N-1,-1,-1):
    if i + timeTable[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(timeTable[i][1] + dp[i + timeTable[i][0]], dp[i+1])

print(dp[0])