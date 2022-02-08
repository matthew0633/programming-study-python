import sys
input = sys.stdin.readline

E, S, M = map(int,input().split())
year = 0

while(True):
    year += 1
    if E > 15:
        E -= 15
    if S > 28:
        S -= 28
    if M > 19:
        M -= 19
    if (year - E) % 15 == 0 and (year - S) % 28 == 0 and (year - M) % 19 == 0 :
        print(year)
        break

print(-15 % 28)

