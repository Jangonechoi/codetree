import sys

N = int(sys.stdin.read())
# print(N)
S = 0
for i in range(2,N):
    if N % i == 0:
        S += 1
print('N') if S == 0 else print('C')
