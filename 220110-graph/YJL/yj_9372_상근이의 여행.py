import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    #  국가의 수 N, 비행기의 종류 M
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())

    print(N-1)

# ==============================
# https://jinho-study.tistory.com/889
import sys

def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
        # print('grah', graph)
    check = [0]*(N+1)
    check[1] = 0
    cnt = dfs(1, 0)
    print(cnt)


