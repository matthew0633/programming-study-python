# # https://dojinkimm.github.io/problem_solving/2019/09/26/boj-1764-deutbo.html
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

n_list = [sys.stdin.readline().rstrip() for _ in range(n)]
m_list = [sys.stdin.readline().rstrip() for _ in range(m)]
result = []
# print(n_list)
# print(m_list)

# 교차하는 이름들을 찾는다
duplicate = list(set(n_list) & set(m_list))

print(len(duplicate))
for name in sorted(duplicate):
    print(name)

# 원래 코드
# 시간 초과 남
# ----------------------
# for name in n_list:
#     if name in m_list:
#         result.append(name)

# for i in result:
#     print(i)
# print(len(result))