# idea : fibonacci(0), fibonacci(1)의 계산 횟수가 일반 피보나치 점화식과 동일
# 참고 : https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801003%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%ED%95%A8%EC%88%98-DP
import sys
inp = sys.stdin.readline
T = int(inp().rstrip())

def fibonacci(n):
    dp = [(0,0)]*(40+1) # (fibonacci(0)횟수, fibonacci(1) 횟수)
    dp[0] = (1,0)
    dp[1] = (0,1)
    for i in range(2, n+1):
        dp[i] = (dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]) # dp[i-1]+dp[i-2]
    return dp[n]

for _ in range(T):
    n = int(inp().rstrip())
    a, b = fibonacci(n)
    print(a, b)



# def fibonacci(n):
#     global cnt0, cnt1
#     if n==0:
#         cnt0+=1
#         return 0
#     elif n==1:
#         cnt1+=1
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# for _ in range(T):
#     n = int(inp().rstrip())
#     cnt0, cnt1 = 0, 0
#     _ = fibonacci(n)
#     print(cnt0, cnt1)
