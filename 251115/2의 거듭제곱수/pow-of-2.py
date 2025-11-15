import sys

N = int(sys.stdin.read())
S = 1

while True:
    if N % (N**0.5) == 0:
        S += 1
        N = N**0.5
    else:
        break

print(S)