"""
idea : 안익은 토마토 위치 queue에 추가 후 bfs 수행
"""
from collections import deque
import sys

inp = sys.stdin.readline
m, n = map(int, inp().rstrip().split())
arr = [list(map(int, inp().rstrip().split())) for _ in range(n)]

# 배열에서 토마토 찾기 (1)
locs = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            locs.append((i,j,0))

dr = [0,0,1,-1]
dc = [1,-1,0,0]

# bfs : 토마토 인접 익음 처리
def bfs(locs):
    q = deque(locs)
    max_cnt = 0
    while q:
        r, c, cnt = q.popleft()
        max_cnt = max(max_cnt, cnt)
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<n and 0<=nc<m and arr[nr][nc]==0:
                q.append((nr, nc, cnt+1))
                arr[nr][nc] = cnt+1
    return max_cnt

max_cnt = bfs(locs)

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            print(-1)
            exit()

print(max_cnt)