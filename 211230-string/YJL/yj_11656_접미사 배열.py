import sys

suffix = sys.stdin.readline().rstrip()
suffix_list = [suffix[i:] for i in range(len(suffix))]

# print(suffix_list)
print('\n'.join(sorted(suffix_list)))