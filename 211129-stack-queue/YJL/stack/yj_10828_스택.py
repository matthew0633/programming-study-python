import sys
n = int(sys.stdin.readline())

stack_list = list()

def size():
    print(len(stack_list))

def push(data): 
    return stack_list.append(data)

def pop():
    if len(stack_list)==0:
        print(-1)
    else:
        print(stack_list.pop())

def empty():
    if len(stack_list) == 0:
        print(1)
    else:
        print(0)

def top():
    # 맨 끝은 -1 -> 리스트 사이즈에 상관없이
    if len(stack_list) == 0:
        print(-1)
    else:
        print(stack_list[-1])
    

for i in range(n):
    command = sys.stdin.readline().split()
    
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    else:
        top()