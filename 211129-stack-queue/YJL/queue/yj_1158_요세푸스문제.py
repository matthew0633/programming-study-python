# (N, K)-요세푸스 순열
# (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>
# 답지 확인 후 코드 이해...
# https://infinitt.tistory.com/213

# N명의 사람들이 있고, K를 주기로 사람들을 제거하는 문제였다. 
# 이때 K(주기)가 사람의 인원수를 초과하면
# 사람의 인원수로 나눈 나머지로 값을 초기화해주면 된다. 

import sys
n, k = map(int, sys.stdin.readline().split())
permu = [i for i in range(1, n+1)] # 맨 처음에 원에 앉아있는 사람들

result = [] # 제거된 사람들을 넣을 배열
num = 0 # 제거될 사람의 인덱스 번호

for i in range(n):
    num += k - 1
    print('num: ', num)
    if num >= len(permu): # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈 
        num = num % len(permu)

    result.append(str(permu.pop(num)))
    # print('permu.pop(num) :', permu.pop(num))

print("<",", ".join(result)[:],">", sep='')
