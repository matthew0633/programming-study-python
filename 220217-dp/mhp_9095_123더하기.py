"""
idea: 1,2,3 을 (1,2,3)의 합으로 나타낼 수 있는 수를 구하고 이를 활용하여 dp[n]의 점화식 구성
dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
"""
import sys
inp = sys.stdin.readline
T = int(inp().rstrip())

def get_dp():
    dp = [0]*11
    # 1,2,3 을 나타낼 수 있는 가짓수
    dp[1] = 1 
    dp[2] = 2 
    dp[3] = 4

    # dp[n] 점화식 : 1, 2, 3의 합으로 n을 나타낼 수 있는 가짓수
    for i in range(4, 11):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp

dp = get_dp()
for _ in range(T):
    n = int(inp().rstrip())
    print(dp[n])