"""
idea : 모든 수를 순회하며 '666' 들어간 수 count
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

i = 1
cnt = 0
while True:
    if '666' in str(i):
        res = i
        cnt+=1
        if cnt==n:
            break
    i+=1

print(res)
