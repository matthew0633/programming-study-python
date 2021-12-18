import sys

delivery = int(sys.stdin.readline())
result = 0

while delivery >= 0:
    # print('delivery % 5', delivery % 5)
    if delivery % 5 == 0:
        result += int(delivery // 5)
        print(result)
        break
    print('delivery:', delivery)
    delivery -= 3
    result += 1
    
else:
    print(-1)