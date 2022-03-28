# 다익스트라 : 하나의 정점에서 출발해서 다른 모든 정점으로의 최단 거리
# 플로이드 와샬 : 모든 정점에서 출발해서 다른 모든 정점으로의 최단 거리 -> 기본적으로 다이나믹 프로그래밍

import sys
from collections import deque
n = int(sys.stdin.readline()) # 정점의 개수 N
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # 그래프 

# y 기준으로 x 탐색
def find(start, end, maps):
    queue = deque()
    queue.append(start)
    visited = set()
    while queue:
        x = queue.popleft()
        visited.add(x)
        next_row = maps[x]
        for i in range(len(next_row)):
            if next_row[i] == 1:
                # 갈 수 있는 곳이 도착지일 경우
                if i == end:
                    return 1
                # 아직 방문하지 않은 row일 경우
                elif i not in visited:
                    queue.append(i)
                    visited.add(i)
    return 0
answer = [[0 for _ in range(n)] for _ in range(n)]
for y in range(n):
    for x in range(n):
        print(y, x, maps)
        answer[y][x] = find(y, x, maps)
    print(*answer[y])
