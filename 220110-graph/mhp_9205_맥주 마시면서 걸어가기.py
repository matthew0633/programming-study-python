"""
idea : 시작점부터 이동 가능한 지점들에 대해 bfs 수행
- '직사각형 형태' => 배열 떠올렸어야
- 'togo'에 시작점 미포함 -> 첫지점 방문표시 필요X
"""
import sys
from collections import deque

def bfs(x0, y0, togo):

    # 맥주 개수
    beer = 20

    # 시작점
    q = deque([(x0, y0)])

    # 방문 check
    v = [False]*len(togo)

    while q:
        x, y = q.popleft()

        # 목적지 방문 가능
        if v[-1]:
            return 'happy'

        for idx, (nx, ny) in enumerate(togo):
            l1 = abs(nx-x) + abs(ny-y)
            
            # 다음 지점 미방문 and 도착가능
            if not v[idx] and (beer*50 >= l1):
                q.append((nx,ny))
                v[idx] = True
    return 'sad'

inp = sys.stdin.readline

# 테스트 케이스 개수
t =  int(inp().rstrip())

for _ in range(t):

    # 편의점 개수
    n = int(inp().rstrip())

    # 시작지점
    x0, y0 = map(int, inp().rstrip().split())

    # 편의점 + 목적지 좌표 저장
    togo = []

    # 편의점 좌표 저장
    for _ in range(n):
        x1, y1 = map(int, inp().rstrip().split())
        togo.append((x1, y1))

    # 목적지 좌표
    x, y = map(int, inp().rstrip().split())

    # 목적지 추가
    togo.append((x,y))

    # 편의점, 목적지에 대해 bfs
    print(bfs(x0, y0, togo))