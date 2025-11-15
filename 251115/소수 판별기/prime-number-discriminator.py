import sys

N = int(sys.stdin.read())

# print(N)

for i in range(2,N):
    if N % i == 0:
        print('C')
        break
    elif i == N-1:
        print('P')

    