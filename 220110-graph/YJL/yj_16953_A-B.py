# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

import sys

A, B = map(int,sys.stdin.readline().split())

count = 1
while True:
    if A == B:
        break
    elif A > B or (B % 10 != 1 and B % 2 != 0):
        count = -1
        break
    elif B % 10 == 1:
        B //= 10
        count+=1
    elif B % 2 == 0:
        B //= 2
        count+=1
    
print(count)