import sys

N = int(sys.stdin.read())

# print(N)

for _ in range(2):
    for _ in range(N):
        for _ in range(N):
            print('*', end='')
        print()
    print()
    

