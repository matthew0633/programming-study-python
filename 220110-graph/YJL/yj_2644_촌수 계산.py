# 첫째 줄에는 전체 사람의 수 n
# 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호
# 셋째 줄에는 부모 자식들 간의 관계의 개수 m
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y
# 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호

import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
a,b = map(int, input().split())
m = int(input())

chonsu = defaultdict(list)

for _ in range(m):
    x, y = map(int, input().split())
    chonsu[x].append(y)
    chonsu[y].append(x)

# print(chonsu)

def chonsu_calculate(v, target, graph):
    count = 0
    visited, need_visit = list(), list()
    need_visit.append((count, v))
    while need_visit:
        count, start = need_visit.pop(0)
        if start == target:
            return count
        for i in graph[start]:
            if i not in visited:
                visited.append(i)
                need_visit.append((count+1, i))
                # print('visited', visited)
                # print('need_visit', need_visit)
    return -1
        
print(chonsu_calculate(a, b, chonsu))