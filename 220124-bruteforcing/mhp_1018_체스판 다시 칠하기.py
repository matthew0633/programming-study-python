"""
idea : 첫칸이 B or W 일 때 (r+c)가 짝수, 홀수인 칸에 따라 규칙을 만족하는지 검사
"""

import sys
inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())
g = [inp().rstrip() for _ in range(n)]

def get_min(g,i,j):
    # 첫칸이 W, B일 때 바꿔야할 칸 개수
    wstart = 0
    bstart = 0

    for p in range(i, i+8):
        for q in range(j, j+8):
            # 합이 짝수일 때, 홀수일 때
            if (p+q)%2 == 0:
                if g[p][q] != 'W':
                    wstart += 1  
                if g[p][q] != 'B': 
                    bstart += 1
            else :
                if g[p][q] != 'B': 
                    wstart += 1
                if g[p][q] != 'W': 
                    bstart += 1
    return min(wstart, bstart)

cnt = 999999
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = min(cnt, get_min(g, i, j))

print(cnt)