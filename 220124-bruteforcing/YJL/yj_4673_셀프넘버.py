natural_num = set(range(1, 10001))
generatd_num = set()

for i in range(1, 10001): # i = 850
    for j in str(i):	  # j = '8', '5', '0'
        i += int(j)	      # 850 + 8 + 5 + 0 = 863 = i
    generatd_num.add(i)	  # 생성자가 있는 숫자들

self_num = sorted(natural_num - generatd_num)
for k in self_num:
    print(k)