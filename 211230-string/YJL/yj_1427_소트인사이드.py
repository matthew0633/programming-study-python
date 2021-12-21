import sys

number = sys.stdin.readline().rstrip()
print(''.join(sorted(number, reverse=True)))

