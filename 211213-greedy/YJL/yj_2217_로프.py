import sys
N = int(sys.stdin.readline())

rope_list = []
for _ in range(N):
    rope_list.append(int(sys.stdin.readline()))

result_list=[]
rope_list.sort(reverse=True)

for i in range(N):
    result_list.append(rope_list[i] * (i+1))

print(max(result_list))