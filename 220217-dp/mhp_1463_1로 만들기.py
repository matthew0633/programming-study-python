"""
idea : dp[i] i일 때 1이 되기까지 필요한 연산 수
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
dp = [0]*(n+1)
cnt=2
for i in range(2, n+1):
    dp[i] = min(n+1 if i%3 else dp[i//3]+1, 
                    n+1 if i%2 else dp[i//2]+1, 
                    dp[i-1]+1)
print(dp[n])