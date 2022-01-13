"""
idea : 
- 모두 연결이므로 dfs 수행을 count
- 모두 연결이므로 단순히 (V-1)을 출력해도 정답
"""
import sys

def dfs(g, v):
    stack = [v]
    visited = [0]*(n+1)
    visited[v] = 1
    cnt = 0
    while stack:
        v = stack.pop()
        for nx in g[v]:
            if not visited[nx]:
                visited[nx]=1
                stack.append(nx)
                cnt+=1
    return cnt

inp = sys.stdin.readline
t = int(inp().rstrip())

for _ in range(t):
    n,m = map(int, inp().rstrip().split())

    # 모두 연결 : n-1 출력
    # print(n-1)
    # continue
    
    g = [[] for _ in range(n+1)]

    for _ in range(m):
        a,b = map(int, inp().rstrip().split())
        g[a].append(b)
        g[b].append(a)
    
    print(dfs(g, 1))