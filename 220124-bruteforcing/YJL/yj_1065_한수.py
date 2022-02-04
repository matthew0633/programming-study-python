import sys
input = sys.stdin.readline

num = int(input())
hansu = 0 

for i in range(1, num+1):
    if i <= 99:
        hansu += 1
    else:
        numPart = list(map(int, str(i)))
        if numPart[1] - numPart[0] == numPart[2] - numPart[1]:
            hansu += 1

print(hansu)