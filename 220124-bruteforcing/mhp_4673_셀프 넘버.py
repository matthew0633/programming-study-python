"""
idea : 1000까지 순회하며, d(n) 결과값들에 대해 True, False 표시, 이후 True 값(셀프넘버) 출력
"""

# 셀프넘버 True 표시
res = [False]+[True for _ in range(10000+1)]

for i in range(1, 10001):
    li = map(int, str(i))
    tot = i + sum(li)

    # d(n)이 10000이 넘지 않을 때 only
    if tot<=10000:
        res[tot]=False

for i in range(1, 10001):
    if res[i]:
        print(i)