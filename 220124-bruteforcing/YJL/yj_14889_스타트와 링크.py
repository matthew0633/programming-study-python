import sys
from itertools import combinations #조합 함수
input = sys.stdin.readline

N = int(input())
member = [i for i in range(N)]
power_list = []

#팀 생성해주기
for _ in range(N):
    power_list.append((list(map(int, input().split()))))

result = int(1e9)
for t1 in combinations(member, N//2):
    # start, link 능력치
    start, link = 0, 0
    t2 = list(set(member) - set(t1))
    # 스타트 팀
    for t in combinations(t1, 2):
        start += power_list[t[0]][t[1]]
        start += power_list[t[1]][t[0]]
    # 링크 팀
    for t in combinations(t2, 2):
        link += power_list[t[0]][t[1]]
        link += power_list[t[1]][t[0]]
    result = min(result, abs(start - link))
print(result)