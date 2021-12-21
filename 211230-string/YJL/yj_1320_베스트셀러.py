import sys
# from operator import itemgetter

N = int(sys.stdin.readline())
N_list = [sys.stdin.readline().rstrip() for _ in range(N)]

count = {}

for i in N_list:
    try: count[i] += 1
    except: count[i] = 1

# print(count)
# {'top': 4, 'kimtop': 1}
maxVal = max(count.values())
# print(sorted(count, key=itemgetter(1)))
result_arr = []

for k, v in count.items():
    if v == maxVal:
        result_arr.append(k)

print(sorted(result_arr)[0])