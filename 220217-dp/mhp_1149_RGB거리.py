"""
idea: 각 집마다 색상 모두 이전집의 다른 색과 모두 최솟값 비교로 비용 갱신
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
dp = [list(map(int, inp().rstrip().split())) for _ in range(n)]

for i in range(1,n):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))