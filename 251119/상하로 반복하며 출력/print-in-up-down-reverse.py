import sys

N = int(sys.stdin.read())
# print(N)

for i in range(N):
    for j in range(N):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 == 0):
            print(i+1,end='')
        elif (i % 2 == 0 and j % 2 != 0) or (i % 2 != 0 and j % 2 !=0):
            print(N-i,end='')
    print()