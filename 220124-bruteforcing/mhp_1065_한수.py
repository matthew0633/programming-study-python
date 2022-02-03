"""
idea : 각 자리수 간의 공차 비교로 한수 여부 check
"""
import sys
inp = sys.stdin.readline
n = int(inp().rstrip())

def ishansu(x:str):
    li = list(map(int, x))
    for i in range(len(li)-1):
        if i==0:
            d=li[i+1]-li[i]
            continue
        if li[i+1]-li[i]!=d:
            return False
    return True

cnt = 0
for i in range(1, n+1):
    if ishansu(str(i)):
        cnt+=1

print(cnt)

"""
if n<100:
    print(n)
    exit()

cnt=99
for i in range(100, n+1):
    if i==1000:
        continue

    a, b, c = map(int, str(i))
    if (b-a)==(c-b):
        cnt+=1
print(cnt)
"""