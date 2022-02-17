"""
idea: dp[i-1]+li[i]와 li[i] 중 최댓값을 dp[i]로 갱신
참고: https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801912%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%97%B0%EC%86%8D-%ED%95%A9-DP
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
li = list(map(int, inp().rstrip().split()))
dp = [0]*n
dp[0] = li[0]

for i in range(1, n):
    dp[i] = max(dp[i-1]+li[i], li[i])
print(max(dp))