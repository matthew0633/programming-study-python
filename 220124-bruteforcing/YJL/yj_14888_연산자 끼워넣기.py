# https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9

def caluculate(cnt, total, plus, minus, multiply, divide):
    global maximum, minimum
    if cnt == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        caluculate(cnt + 1, total + num[cnt], plus - 1, minus, multiply, divide)
    if minus:
        caluculate(cnt + 1, total - num[cnt], plus, minus - 1, multiply, divide)
    if multiply:
        caluculate(cnt + 1, total * num[cnt], plus, minus, multiply - 1, divide)
    if divide:
        caluculate(cnt + 1, int(total / num[cnt]), plus, minus, multiply, divide - 1)


caluculate(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)