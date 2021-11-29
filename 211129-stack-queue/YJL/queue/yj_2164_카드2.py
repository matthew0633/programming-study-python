import sys
from collections import deque
n = int(sys.stdin.readline())

#### 시간초과 발생! 이유 - card 배열 생성 시간에서 초과 ####
#### deque로 해결 
card_list = deque([i for i in range(1, n+1)])
# print('card_list', card_list)

while len(card_list) > 1:
    
    if len(card_list) != 1:
        # 맨 첫번째 버리기
        card_list.popleft()
        # print('1: ', card_list)
        # 그 다음 첫번째 수 맨 뒤로 보내기
        card_list.append(card_list.popleft())
        # print('2: ', card_list)
    

print(card_list.popleft())