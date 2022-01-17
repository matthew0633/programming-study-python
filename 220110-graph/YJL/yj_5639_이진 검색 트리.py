# 전위 순회 (루트-왼쪽-오른쪽) 루트를 방문 -> dfs
# 후위 순회 (왼쪽-오른쪽-루트) -> bfs? 근데 반대루

# https://donghak-dev.tistory.com/71
# 문제 풀이 : 주어진 순회를 입력 받아 이를 이진 트리임에 유의하여 더 커지는 순간이 자신의 루트라는 것을 생각하여 재 구성하여 출력하면 된다.
def solution(start, end):
    if start > end:
        return

    div = end + 1

    for i in range(start + 1, end + 1):
        # 루트 보다 큰 지점 --> 오른쪽 서브 트리
        if tree[start] < tree[i]:
            div = i
            break

    solution(start + 1, div - 1)
    solution(div, end)
    print(tree[start])


import sys
sys.setrecursionlimit(10 ** 9)
# [파이썬 코딩테스트 팁] sys.setrecursionlimit
# https://fuzzysound.github.io/sys-setrecursionlimit
# 만약 재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수이다. 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다.

tree = []
count = 0
while count <= 10000:

    try:
        temp = int(input())
    except:
        break
    tree.append(temp)
    count += 1

solution(0, len(tree) - 1)