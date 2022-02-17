"""
idea : 이전계단을 밟는 경우와, 밟지 않는 경우 두가지로 점화식 구성
주의 : 계단의 개수가 n<2인 경우도 있으므로 dp, s 리스트의 길이는 최대길이인 301로 구성해야 (Indexerror)

i-1(x):        i-2(v) i-1(x) i(v)
i-1(v): i-3(v) i-2(x) i-1(v) i(v)

dp[1] = s[1] # base
dp[2] = max(s[2], dp[1]+s[2]) # base
dp[3] = max(dp[0]+s[2]+s[3], dp[1]+s[3])
"""

import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

dp = [0]*(300+1)
s = [0]*(300+1)

for i in range(1, n+1):
    s[i] = int(inp().rstrip())

dp[1] = s[1]

for i in range(3, 300+1):
    dp[i] = max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    if i==n:
        break

print(dp[n])