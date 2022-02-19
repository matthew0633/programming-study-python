"""
idea: 각 층의 가장 왼쪽, 오른쪽, 가운데에 따른 update case 분기
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())
tri = [list(map(int, inp().rstrip().split())) for _ in range(n)]
for i in range(1, len(tri)):
    for j in range(i+1): # idx1 층에 idx1까지 순회
        if j==0:
            tri[i][j] += tri[i-1][j] # tri[1][0] += tri[0][0]
        elif j==i:
            tri[i][j] += tri[i-1][j-1] # tri[1][1] += tri[0][0]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
print(max(tri[-1]))

