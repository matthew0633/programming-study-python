# 맥주 한 박스에는 20개가 들어있다
# https://chldkato.tistory.com/44

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    q, c = deque(), []
    q.append([x, y, 20])
    c.append([x, y, 20])
    while q:
        x, y, beer = q.popleft()
        if x == x1 and  y == y1:
            print('happy')
            return
        for nx, ny in songdo:
            if [nx, ny, 20] not in c:
                l1 = abs(nx - x) + abs(ny - y)
                if beer * 50 >= l1:
                    q.append([nx, ny, 20])
                    c.append([nx, ny, 20])
    print("sad")
    return

# 테스트 케이스의 개수 t
t = int(input()) 

while t:
    # 맥주를 파는 편의점의 개수 n
    n = int(input())
    x0, y0 = map(int, input().split()) 
    songdo = []
    #  n+2개 줄에는 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표
    for _ in range(n):
        x, y = map(int, input().split())
        songdo.append([x, y])
    x1, y1 = map(int, input().split())
    songdo.append([x1, y1])
    bfs(x0, y0)
    t -= 1

