import sys

R,C = map(int, sys.stdin.read().split())

# print(R,C)

for _ in range(R):
    for _ in range(C):
        print('*', end = ' ')
    print()