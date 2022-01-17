# 유저의 수 N
# 친구 관계의 수 M
# 둘째 줄부터 M개의 줄에는 친구 관계가 주어진다. 
# 친구 관계는 A와 B로 이루어져 있으며, A와 B가 친구라는 뜻이다

# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# N, M = map(int, input().split())

# friends = defaultdict(list)
# result = defaultdict(list)

# for _ in range(M):
#     a, b = map(int, input().split())
#     friends[a].append(b)
#     friends[b].append(a)

# print(friends)

# def kabin_bacon(end):
#     count = 0
#     visited, need_visit = list(), list()
#     need_visit.append(1)
#     while need_visit:
#         print('count', count)
#         print('need_visit', need_visit)
#         print('visited', visited)
#         num = need_visit.pop(0)
#         visited.append(num)
#         if num == end:
#             return count
#         if num not in visited:
#             need_visit.extend(friends[num])
#             count += 1

# print(kabin_bacon(N))

# https://hello-i-t.tistory.com/93
# 정답 코드
import sys 
from collections import defaultdict 
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
graph = defaultdict(list)

for _ in range(M): 
    a, b = map(int, input().split()) 
    graph[a].append((b, 1)) 
    graph[b].append((a, 1))

# print('graph', graph)

# 다익스트라 알고리즘 구현
# 다익스트라 알고리즘? -> 최단 경로 찾기 알고리즘
answer = []
for k in range(1, N+1): 
    # 0 -> count , k -> 노드
    # N -> 유저가 5이면 1~5 거리 수 구하기
    # [(0,1)] [(0,2)] [(0,3)] [(0,4)] [(0,5)]
    queue = [(0, k)] 
    visited = defaultdict(int) 
    while queue: 
        time, node = heapq.heappop(queue)
        if node not in visited: 
            visited[node] = time 
            for v, w in graph[node]: 
                # print('v,w', v, w)
                heapq.heappush(queue, (time+w, v)) 
    # print('visited', visited)
    # k = 1의 한 바퀴 {1: 0, 3: 1, 4: 1, 2: 2, 5: 2})
    answer.append((sum(visited.values()), k)) 

# print(answer)
answer.sort() 
# print(answer)
print(answer[0][1])