import sys

N, K = map(int, sys.stdin.readline().split())
coin_list = []
for i in range(N):
    coin_list.append(int(sys.stdin.readline().rstrip()))

coin_list.sort(reverse=True)

result = 0
for coin in coin_list:
    money = K // coin
    result += money
    K -= coin * money

print(result)