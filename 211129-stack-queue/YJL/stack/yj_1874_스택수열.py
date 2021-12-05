# 문제 이해 안되서 답지 보고 이해함
import sys
n = int(sys.stdin.readline())

count = 1
stack = []
result = []
message = True

for i in range(n):
    num = int(sys.stdin.readline())
    # print('count', count)

    while count <= num:
        stack.append(count)
        result.append("+")
        count += 1
        # print('while stack: ', stack)

    if(stack[-1] == num):
        stack.pop()
        # print('stack[-1]: ', stack)
        result.append("-")
    else:
        print('num', num)
        message = False

# print('stack: ', stack)

if message == False:
    print('NO')
else:
    for res in result:
        print(res)