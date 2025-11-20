import sys

N = int(sys.stdin.read())
# print(N)
C = 65
for i in range(N):
    for j in range(i+1):
        print(chr(C),end='')
        C += 1
        if C == 91:
            C = 65
    print()
