import sys

N = int(sys.stdin.read())
# print(N)
C = ''
for i in range(N):
    for j in range(N):
        C = chr(64+i*N+j+1)
        print(C, end='')
    print()
