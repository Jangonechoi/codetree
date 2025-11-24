import sys

N = list(map(int, sys.stdin.read().split()))
# print(N) [3, 1, 4, 6, 8, 2, 5]
c = N[0]
del N[0]
# print(N) [1, 4, 6, 8, 2, 5]
s = 1
for i in range(c):
    for j in range(N[1+i*2]-N[0+i*2]+1):
        s = s * (N[0+i*2]+j)
    print(s)
    s = 1

