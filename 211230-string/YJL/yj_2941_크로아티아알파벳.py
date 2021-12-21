# 문제 이해 못함
# https://hongku.tistory.com/255

Croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()

for c in Croatia:
    alpha = alpha.replace(c, '*')
    # print(alpha)

print(len(alpha))
