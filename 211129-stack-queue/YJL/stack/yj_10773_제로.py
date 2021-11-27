import sys
n = int(sys.stdin.readline())
num_stack= []

for i in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        num_stack.pop()
    else:
        num_stack.append(num)

print(sum(num_stack))
