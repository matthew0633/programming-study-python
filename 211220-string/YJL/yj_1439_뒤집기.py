import sys
T = int(sys.stdin.readline())

reverse_list = []

for _ in range(T):
    str = sys.stdin.readline().rstrip()
    words = list(str.split())
    reverse_words = []

    for word in words:
        reverse_words.append(word[::-1])

    answer = " ".join(reverse_words)
    reverse_list.append(answer)

for re in reverse_list:
    print(re)