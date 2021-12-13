# https://pacific-ocean.tistory.com/228
# 최솟값을 만들기 위해서는 - 기준으로 괄호를 치면 된다.

sik = input().split('-')
# print(sik)
# ['55', '50+40']
num = []
for i in sik:
    cnt = 0
    plusNum = i.split('+')
    # print(s)
    # ['55']
    # ['50', '40']
    for j in plusNum:
        cnt += int(j)
    num.append(cnt)
result = num[0]
# print(num) # [55, 90]
# print(result) # 55

for n in range(1, len(num)):
    # print('num[n]', num[n]) # 90
    result -= num[n]

print(result)


