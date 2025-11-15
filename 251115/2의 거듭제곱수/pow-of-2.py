import sys

N = int(sys.stdin.read())
S = 0

while True:
    if N % 2 == 0:
        S += 1
        N = N/2
    else:
        break

print(S)