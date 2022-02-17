"""
idea: 계단오르기와 비슷하게 연속 3개를 마시지 못하는 DP 구현, 
but 마지막 잔을 무조건 마실 필요가 없다는 것에서 차이존재

따라서 dp[i-1]+0 과도 최댓값을 비교해야함

dp[i] = max(dp[i-2]+li[i], dp[i-3]+li[i-1]+li[i], dp[i-1])

"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
li = [int(inp().rstrip()) for _ in range(n)] + [0]*(10001-n)
dp = [0]*10001
dp[0] = li[0]
dp[1] = sum(li[:2])
dp[2] = max(li[0]+li[2], li[1]+li[2], dp[1])
#dp[3] = max(dp[1]+li[3], dp[0]+li[2]+li[3], li[1]+li[2]+li[3])

for i in range(3, n):
    dp[i] = max(dp[i-2]+li[i], dp[i-3]+li[i-1]+li[i], dp[i-1])

print(dp[n-1])