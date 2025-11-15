import sys

N = int(sys.stdin.read())
# print(N)

for i in range(N):
    for j in range(i*2+1):
        print("*",end='')
    print()
