import sys

N = int(sys.stdin.read())

# print(N)

for i in range(N):
    for _ in range(N-i):
        print('* ',end='')
    print()