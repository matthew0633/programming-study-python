"""
idea : graph 생성 후 a에 대하여 bfs 수행, b와 같을 때 count return
"""
import sys
from collections import deque

inp = sys.stdin.readline
n = int(inp().rstrip())
a, b = map(int, inp().rstrip().split())
m = int(inp().rstrip())
g = [[] for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, inp().rstrip().split())
    g[n2].append(n1)
    g[n1].append(n2)

def bfs(a, b):
    q = deque([(a, 0)])
    v = [0]*(n+1)
    while q:
        curr, cnt = q.popleft()
        if curr == b:
            return cnt
        for nx in g[curr]:
            if not v[nx]:
                v[nx]=1
                q.append((nx, cnt+1))
    return -1

print(bfs(a, b))