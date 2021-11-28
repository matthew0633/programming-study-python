import sys
n = int(sys.stdin.readline())

# import queue
# data_queue = queue.Queue()
data_queue= []

for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        data_queue.append(command[1])
    elif command[0] == 'pop':
        if len(data_queue) == 0:
            print(-1)
        else:
            print(data_queue.pop(0))
    elif command[0] == 'size':
        print(len(data_queue))
    elif command[0] == 'empty':
        if len(data_queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(data_queue) == 0:
            print(-1)
        else:
            print(data_queue[0])
    else:
        if len(data_queue) == 0:
            print(-1)
        else:
            print(data_queue[-1])
