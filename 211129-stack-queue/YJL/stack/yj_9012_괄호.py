import sys
n = int(sys.stdin.readline())

for i in range(n):
    input_ps = list(sys.stdin.readline())
    sum = 0
    stack = []
    for p in input_ps:
        if p == "(":
            stack.append(p)
            sum += 1
        elif p == ")":
            if len(stack) != 0:
                stack.pop()
            else:
                stack.append(p)
            sum -= 1

    if len(stack) == 0 and sum == 0:
        print('YES')
    else:
        print('NO')