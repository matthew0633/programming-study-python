"""
idea : node 마다 bfs 실시 후 max_num 에 해당하는 node들을 오름차순으로 출력

시간초과 원인 : 
첫번째 주석처리된 bfs는 로직은 비슷해보이나 if 조건문에 new not in q 로 인해 해당 for문에서 O(N^2)의 복잡도를 가진다
이때 node의 최대개수가 10,000이므로 시간초과가 발생할 수 있다.
따라서 if 조건문에서는 visited만을 수행하도록 하여 for문의 복잡도를 O(N)으로 줄여야한다

"""
import sys
from collections import deque, defaultdict

inp = sys.stdin.readline
n, m = map(int, inp().rstrip().split())

# graph 생성
g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, inp().rstrip().split())
    g[b].append(a)

# # 시간초과 bfs
# def bfs(i):
#     q = deque([i])
#     visited = [0 for _ in range(n+1)] # dummy 추가
#     cnt = 0

#     while q:
#         curr = q.popleft()
#         visited[curr] = 1
#         cnt+=1
#         for new in g[curr]:
#             if visited[new]==0 and new not in q:
#                 q.append(new)
#     return cnt

# bfs
def bfs(i):
    q = deque([i])
    visited = [0 for _ in range(n+1)] # dummy 추가
    cnt = 1
    visited[i] = 1
    while q:
        curr = q.popleft()
        for new in g[curr]:
            if visited[new]==0:
                visited[new] = 1
                cnt+=1
                q.append(new)
    return cnt

results = [] 
max_cnt = 0 

# node별 해킹가능pc들에 대해 bfs
for i in range(1, n+1): 
    cnt = bfs(i)

    # bfs결과가 최대일 때 : node 및 최대 해킹가능개수 갱신
    if cnt > max_cnt: 
        results = [i]
        max_cnt = cnt 
    
    # bfs결과가 기존 max와 같을 때 : node만 추가
    elif cnt == max_cnt: 
        results.append(i)
print(*results)