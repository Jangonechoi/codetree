import sys

N = int(sys.stdin.read())
# print(N)
# cnt = 1
# cnt2 = N*2
for i in range(N):
    for j in range(N):
        if i % 2 == 0:
            print(i*N+1+j,'', end='')
        else:
            print(N*(i+1)-j,'', end='')
    print()