"""
idea : 
- 높이를 첫번째 차원으로 하는 3차원배열+bfs로 풀이
- 2차원 배열 풀이의 실패 이유: bfs에서 if문에 들어가는 row와 height에 대한 정상범위가 상이해서 한번에 일괄 작성 불가
"""
import sys
from collections import deque
inp = sys.stdin.readline
m,n,h = map(int, inp().rstrip().split())

g = [[list(map(int, inp().rstrip().split())) for _ in range(n)] for _ in range(h)]

# 토마토 위치 기록
locs = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k]==1:
                locs.append((i,j,k))

# bfs 수행
def bfs(g, locs, h, m, n):
    q = deque(locs)
    dk = [0,0,0,0,1,-1]
    dr = [0,0,1,-1,0,0]
    dc = [1,-1,0,0,0,0]
    max_cnt = 0
    while q:
        k, r, c = q.popleft()
        max_cnt = max(max_cnt, g[k][r][c])
        for i in range(6):
            nk = k+dk[i]
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nk<h and 0<=nr<n and 0<=nc<m and g[nk][nr][nc]==0:
                q.append((nk, nr, nc))
                g[nk][nr][nc]=g[k][r][c]+1
    return max_cnt

ans = bfs(g, locs, h, m, n)

# 덜익은 토마토 존재 시 -1 출력
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k]==0:
                print(-1)
                exit()

# bfs에서 시작 토마토에 대한 일수를 1로 계산했으므로 -1
print(ans-1)

"""
# 2차원 배열 풀이(실패) - (h*n, m)
"""
# import sys
# from collections import deque

# def bfs(g, locs, m, n):
#     q = deque(locs)
#     dr = [0,0,1,-1,n,-n]
#     dc = [1,-1,0,0,0,0]
#     max_cnt = 0
#     while q:
#         r, c, cnt = q.popleft()
#         max_cnt = max(max_cnt, cnt)
#         for i in range(6):
#             nr = r+dr[i]
#             nc = c+dc[i]

#             
#             if 0<=nr<n and 0<=nc<m and g[nr][nc]==0:
#                 q.append((nr, nc, cnt+1))
#                 g[nr][nc]=1
#     return cnt

# inp = sys.stdin.readline
# m,n,h = map(int, inp().rstrip().split())
# g = [list(map(int, inp().rstrip().split())) for _ in range(n*h)]

# locs = []
# for i in range(h*n):
#     for j in range(m):
#         if g[i][j]==1:
#             locs.append((i,j,0))

# ans = bfs(g, locs, m, n)

# for i in range(n):
#     for j in range(m):
#         if g[i][j]==0:
#             print(-1)
#             exit()
# print(ans)
