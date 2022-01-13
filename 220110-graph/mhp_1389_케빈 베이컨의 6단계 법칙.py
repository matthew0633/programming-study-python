"""
idea : 
- bfs(cnt+1) 또는 플로이드워셜 사용 가능
- 연결여부를 반영한 인접행렬 생성 후 플로이드 워셜 수행 O(N^3), N<=100
"""
import sys
inp = sys.stdin.readline
n,m = map(int, inp().rstrip().split())
mini = float('inf')

# 인접행렬 생성
g = [[mini for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b = map(int, inp().rstrip().split())
    g[b-1][a-1] = 1
    g[a-1][b-1] = 1

# 플로이드 워셜로 최소거리 기록
for k in range(n):
    g[k][k] = 0
    for i in range(n):
        for j in range(n):
            g[i][j] = min(g[i][k]+g[k][j], g[i][j])
            

for i in range(n):
    dist = sum(g[i])
    if dist<mini:
        mini = dist
        person = i

print(person+1)