import sys

N = int(sys.stdin.read())
# print(N)

for i in range(N):
    for j in range(N):
        print(i+1,end='')
    print()