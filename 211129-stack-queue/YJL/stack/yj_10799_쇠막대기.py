# () -> 레이저
# 답지 확인 후 이해-> 레이저로 나눈 후 갯수 구하는 거 코드로 작성 못함
import sys
bar = list(sys.stdin.readline())

stack = []
result = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(bar[i])
    elif bar[i] == ')':
        if bar[i-1] == '(':
            #()라면 (를 pop하고 현재 스택에 들어있는 ( 수만큼 값을 더해준다.
            # if ()라면 레이저 이기에 count 안됨!
            stack.pop()
            result += len(stack)
        else:
            # ) 부분 더하기
            stack.pop()
            result += 1

print(result)