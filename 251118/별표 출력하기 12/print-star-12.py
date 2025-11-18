import sys

N = int(sys.stdin.read())
# print(N)

for i in range(N):
    for j in range(N):
        if (i == 0 and j%2 == 0) or (i <= j and j % 2 == 1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
