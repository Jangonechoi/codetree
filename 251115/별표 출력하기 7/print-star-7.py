import sys
N = int(sys.stdin.read())

for i in range(N):
    for _ in range(i+1):
        print('* ', end='')
    print()