import sys
input = sys.stdin.readline

N = int(input())

# https://velog.io/@kbhoon/%EB%B0%B1%EC%A4%80-1436-%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85-%EC%8A%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 666앞에 입력한 수 N - 1으로 생각함
# 근데 187 -> 66666
# 이 케이스를 보고 어떤 문제인지 파악이 불가

# 1시리즈 666
# 2시리즈 1666
# 3시리즈 2666
# 4시리즈 3666
# 5시리즈 4666
# 6시리즈 5666

# 7시리즈는 물론 6666

# 이 아니고 6660이다.
# 6661,6662,6663 ~

three_six = 666
count = 0
while True:
    if "666" in str(three_six): #three_six 문자열에 666이 있다면?
        count += 1
        # print(count)
    if count == N: #더한 카운트와 입력값이 같다면 탈출
        print(three_six) #three_six 출력
        break
    three_six += 1 #3 666이 포함된 수가 나올 때 까지 three_six를 1씩 증가 시킨다
    # print(three_six)
