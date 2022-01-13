"""
idea : dfs문제, 그러나 모든정점에 대해 모든 정점에 대한 최소거리를 계산하는 플로이드 워셜 응용
(node 최댓값이 100이므로 O(n^3)이어도 시간초과X)

플로이드 워셜 : 
for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if arr[i][k]+arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k]+arr[k][j] 
"""
import sys

inp = sys.stdin.readline
n = int(inp().rstrip())
arr = [list(map(int, inp().rstrip().split())) for _ in range(n)]

for k in range(0, n):
    for i in range(0, n):
        for j in range(0, n):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for i in range(n):
    print(' '.join(map(str, arr[i])))

