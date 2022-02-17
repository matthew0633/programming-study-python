"""
idea : 처음 왼쪽에 2x1, 2x2을 남기는 경우를 더했을 때의 dp[i] 계산
(dp[i]: 2xi를 채우는 방법 수)

dp[i] = dp[i-1]+dp[i-2] # dp[i-1]: 1을 남겼을 때, dp[i-2]: 2를 남겼을 때

참고: https://bada744.tistory.com/83
"""

import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
dp = [0]*1001
dp[1], dp[2] = 1, 2

for i in range(3, 1001):
    dp[i] = dp[i-1]+dp[i-2]
    if i==n:
        break
print(dp[n]%10007)