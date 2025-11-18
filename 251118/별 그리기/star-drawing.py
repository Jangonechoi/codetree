import sys

N = int(sys.stdin.read())
# print(N)
for i in range(N):
    for _ in range(N-1-i):
        print(' ', end='')
    for _ in range((i+1)*2-1):
        print('*', end='')
    print()

for i in range(N-1):
    for _ in range(i+1):
        print(' ', end='')
    for _ in range((N-1-i)*2-1):
        print('*', end='')
    print()
