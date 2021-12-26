# S = input()
# word = list(S.split())
# reverse_words = []
# search = re.findall('<(.+?)>', S)

# https://kongpowder.tistory.com/128
import re 
pat = re.compile('<[a-zA-Z0-9 ]+>|[a-zA-Z0-9 ]') 
objs = pat.findall(input()) 
# print(objs)
# ['<open>', 't', 'a', 'g', '<close>']
result = '' 
interval = '' 
cnt = 1 

for obj in objs: 
    if obj[0] == '<': # 기존에 저장되어있던 문자열(interval) 뒤집어 담기 
        result += interval[::-1] # <문자열> 담기 
        result += obj # interval 초기화 
        interval = '' 
        print(result) # <open>gat<close>
    else: # 공백일 경우, 
        if obj == ' ': # 기존에 저장되어있던 문자열(interval) 역순 + 공백 담기 
            result += interval[::-1] + obj # interval 초기화 
            interval = '' # 리스트의 마지막인 경우, 
            # print('if:', result)
            # if: noojkeab 
            # if: noojkeab enilno
        elif cnt == len(objs): 
            interval += obj 
            result += interval[::-1] 
            interval = '' 
            # print('elif:', result)
            # elif: noojkeab enilno egduj
        else: # 문자를 뒤집기 위해 변수에 담는다 
            interval += obj 
            # print('else:', interval)
            # t
            # ta
            # tag
    cnt += 1

print(result)