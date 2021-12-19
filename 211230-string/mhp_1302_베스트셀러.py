from collections import Counter
import sys

inp = sys.stdin.readline
n = int(inp().rstrip())
books = [inp().rstrip() for _ in range(n)]

d = sorted(list(Counter(books).items()), key = lambda x: (-x[1], x[0]))
print(d[0][0])
