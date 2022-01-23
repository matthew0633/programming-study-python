# https://god-gil.tistory.com/62

#1. 크기가 N*M이고, 흰색과 검은색으로 막 칠해져있는 보드판이 있다.
#2. 이 보드판을 잘라서 8*8크기의 체스판으로 만들려고 한다.
#3. 체스판은 흰색과 검은색이 번갈아가며 체크무늬를 이루어야 한다.
#4. 보드판을 잘라서, 체스판을 만들기 위해서 알맞게 색을 고쳐서 체크무늬를 만들어야 한다.
#5. 고쳐야 하는 색의 최소값을 구하라.

N, M = map(int, input().split())
board = list()
for i in range(N):
    board.append(input())
repair = list()

for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        first_W = first_W+1
                    if board[k][l] != 'B':
                        first_B = first_B + 1
                else:
                    if board[k][l] != 'B':
                        first_W = first_W+1
                    if board[k][l] != 'W':
                        first_B = first_B + 1
        repair.append(first_W)
        repair.append(first_B)

print(min(repair))