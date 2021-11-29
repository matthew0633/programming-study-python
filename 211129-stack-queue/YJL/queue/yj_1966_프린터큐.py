# 문서의 갯수 N
# 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
#### 문제 이해 불가 답지 확인 후 이해 ####
# https://assaeunji.github.io/python/2020-05-04-bj1966/

# 3           -> 3번 테스트 할 것
# 1 0         -> n = 1, m = 0
# 5           -> 중요도 = 5
# 4 2         -> n = 4, m = 2
# 1 2 3 4     -> 중요도 = 1 2 3 4
# 6 0         -> n = 6, m = 0
# 1 1 9 1 1 1 -> 중요도 = 1 1 9 1 1 1
import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m = list(map(int, sys.stdin.readline().split()))
    imp = list(map(int, sys.stdin.readline().split()))
    # idx 변수 생성: 문서마다 고유 인덱스를 생성
    idx = list(range(len(imp)))
    # m번째 인덱스를 target으로 둠
    idx[m] = 'target'

    # order 초기화(순서)
    order = 0

    # while True이므로 무한 반복인데 break가 있기 때문에 if절에 걸리는 조건이 맞으면 반복이 중단된다.
    while True:
         # 만약 imp의 첫 번째 값이 가장 크다면 order를 하나 증가시킨다.
        if imp[0]==max(imp):
            order += 1
                        
            # idx의 첫 번째 값이 target이라면
            if idx[0]=='target':
                # order를 출력하고 반복을 중단한다.
                print(order)
                break
            # 그렇지 않다면 imp와 idx의 첫 번째 값을 제거한다.
            else:
                imp.pop(0)
                idx.pop(0)

         # idx의 첫번째 값이 target이 될 때까지 반복된다.
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))  
