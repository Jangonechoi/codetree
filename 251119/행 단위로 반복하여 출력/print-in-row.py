import sys

N = int(sys.stdin.read())
# print(N)

for i in range(N):
    for j in range(1,N+1):
        print(j, end='')
    print()