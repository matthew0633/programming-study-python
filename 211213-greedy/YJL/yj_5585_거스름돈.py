import sys

taro = 1000
#  500엔, 100엔, 50엔, 10엔, 5엔, 1엔
coin_list = [500, 100, 50, 10, 5, 1]
change = int(sys.stdin.readline())
money = taro - change
total = 0

for coin in coin_list:
    coin_num = money // coin
    total += coin_num
    money -= coin_num * coin

print(total)
