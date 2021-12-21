import sys

N = int(sys.stdin.readline())
count = 0

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    groupArr = []
    check = 0

    for w in word:
        if w not in groupArr:
            groupArr.append(w)
            
        else:
            if groupArr[-1] != w:
                check -= 1
            else:
                check += 1

    if check == 0 and len(word) == len(groupArr):
        # new와 abab는 다른 경우
        count += 1
    elif check > 0:
        count += 1         

print(count)

# ----------- answer -----------
# https://ooyoung.tistory.com/79

n = int(input())

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1):  # 인덱스 범위 생성 : 0부터 단어개수 -1까지 
        if word[index] != word[index+1]:  # 연달은 두 문자가 다른 때,
            new_word = word[index+1:]  # 현재글자 이후 문자열을 새로운 단어로 생성
            # print(new_word, new_word.count(word[index]))
            # bab 1
            # ab 1
            # b 0
            if new_word.count(word[index]) > 0:  # 남은 문자열에서 현재글자가 있있다면
                error += 1  # error에 1씩 증가.
    if error == 0:  
        group_word += 1  # error가 0이면 그룹단어
print(group_word)


    
        