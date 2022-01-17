# 가중치그래프(weighted graph) -> 간선에 숫자가 부여된 그래프
# 위 문제에선 가중치 없는 방향 그래프라고 하였으므로 => 그냥 방향 그래프를 뜻한다!

import sys
input = sys.stdin.readline
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# 문제를 이해 했으나 코드로 작성하는 방법을 모르겠어서 
# 코드 참조
# https://jay-ji.tistory.com/24 -> 문제 설명 참조
# https://claude-u.tistory.com/336 -> 코드 참조
# === 플로이드-워셜 알고리즘 ===
# -> 그래프에서 가능한 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘
# https://blog.naver.com/ndb796/221234427842


#플로이드-워셜 알고리즘
# 시작점(i)부터 거치는 점(k)을 거쳐 도착 점(j)으로 가는 길이 있다면 [i][j]는 1로 바꿔주면 된다.
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()