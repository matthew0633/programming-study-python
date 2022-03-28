from collections import deque
import sys

input = sys.stdin.readline

t = int(input()) # 첫째 줄에 테스트 케이스의 개수 t

while t: # 문제를 반복하는 횟수
    n = int(input()) # 맥주를 파는 편의점의 개수 n

    store = [] #  편의점, 펜타포트 락 페스티벌 좌표 store에 담기
    visited = [False] * (n+2) # 방문 처리 기록용
    q = deque() #주어진 그래프를 담는 부분

    x,y = map(int,input().split()) # 상근이네 집, 편의점, 펜타포트 락 페스티벌 좌표

    q.append((x,y)) # 좌표를 저장

    for i in range(n):
        tx,ty = map(int,input().split())
        store.append((tx,ty)) # 편의점, 펜타포트 락 페스티벌 좌표 store에 담기
    
    ex, ey = map(int, input().split())
    flag = False
    size = len(store)
    ### q를 돌릴 때 마다 deque에서 나오는 좌표와 목적지와의 거리의 맨해튼 거리를 확인 후 안에 있다면 flag를 True로 바꿔 happy를 출력
    while q:
        cx, cy = q.popleft() 

        if abs(cx - ex) + abs(cy - ey) <= 1000: 
            flag = True
            break
        for i in range(size):
            if not visited[i] and abs(cx - store[i][0]) + abs(cy - store[i][1]) <= 1000:
                visited[i] = True
                q.append((store[i][0], store[i][1]))
    if flag :
        print("happy")
    else:
        print("sad")
    
    t-=1