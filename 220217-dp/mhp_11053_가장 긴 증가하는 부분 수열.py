"""
idea: LIS (Longest Increasing Subsequence)을 DP로 구현

주의: 
1) dp[i]는 자신(li[i])을 포함한 증가하는 수열의 길이어야 한다 *****
2) dp[n]이 최종 정답이 아니라, 전체 중 max값을 구해야 정답

참고: https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""

import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

li = list(map(int, inp().rstrip().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if li[i]>li[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))