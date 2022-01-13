"""
idea : 두가지 연산값이 b보다 작거나 같을 때 bfs 시행, 
a==b일 때 count return
"""
import sys
from collections import deque
inp = sys.stdin.readline
a, b = map(int, inp().rstrip().split())

def bfs(v):
    q = deque([(v,1)])
    while q:
        v, cnt = q.popleft()

        if v == b:
            return cnt
        
        if v*2<=b:
            q.append((v*2, cnt+1))

        if int(str(v)+'1')<=b:
            q.append((int(str(v)+'1'), cnt+1))

    return -1

print(bfs(a))