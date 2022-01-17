# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토

import sys
input = sys.stdin.readline
from collections import deque
# M은 상자의 가로 칸의 수
# N은 상자의 세로 칸의 수
# H은 두 정수 M,N과 쌓아올려지는 상자의 수
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(box)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def finding_ripe_tomatoes():
    day = 0
    while queue:
        h, n, m = queue.popleft()
        for i in range(6):
            nz = h + dz[i]
            ny = n + dy[i]
            nx = m + dx[i]
            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
                if box[nz][ny][nx] == 0:
                    box[nz][ny][nx] = box[h][n][m] + 1
                    queue.append((nz, ny, nx))

    # print('box', box)

    for h in box:
        # print('h', h)
        for n in h:
            # print('n', n)
            if 0 in n:
                return -1
            else:
                day = max(day, max(n))
    return day - 1


# 3차원 배열...
queue = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                queue.append([h, n, m])

# print(queue)
print(finding_ripe_tomatoes())