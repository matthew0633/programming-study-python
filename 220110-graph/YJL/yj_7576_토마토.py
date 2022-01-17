# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
# 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 
# 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.

# bfs 문제 같음 -> 최단거리
import sys
input = sys.stdin.readline
from collections import deque

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

# print(M, N)
# print(box)

def finding_ripe_tomatoes():    
    day = 0
    while queue:
        # print('queue', queue)
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i] 
            if 0 <= nx < N and 0 <= ny < M:
                if box[nx][ny] == 0:
                    box[nx][ny] = box[a][b] + 1
                    queue.append((nx, ny))
    
    # print(box)

    for b in box:
        if 0 in b:
           return -1
        else:
            day = max(day, max(b))
    
    return day - 1

queue = deque([])        
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])

print(finding_ripe_tomatoes())
