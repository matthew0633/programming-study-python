import sys

document = sys.stdin.readline().rstrip()
search = sys.stdin.readline().rstrip()

# https://assaeunji.github.io/python/2020-05-06-bj1543/
count = 0
index = 0

while index <= (len(document) - len(search)):
    if document[index: index+len(search)] == search:
        count += 1
        index += len(search)  # 단어의 길이만큼 인덱스를 더해주고
    else: # 찾지 못하면
        index += 1  # 1만큼 인덱스를 더해줌

print(count)
