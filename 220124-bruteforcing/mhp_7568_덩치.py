"""
idea : 자신보다 덩치가 큰 사람의 수를 count, 등수는 count+1 
"""
import sys
inp = sys.stdin.readline

n = int(inp().rstrip())
li = [list(map(int, inp().rstrip().split())) for _ in range(n)] # w,h

res = []
for i in range(n):
    cnt = 0
    for j in range(n):
        if i==j:
            continue

        if (li[i][0] < li[j][0]) and (li[i][1] < li[j][1]):
            cnt+=1

    # 내 등수: (큰사람수+1) 등
    res.append(cnt+1)

print(' '.join(map(str, res)))