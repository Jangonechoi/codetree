import sys

N = int(sys.stdin.read())
# print(N)

for i in range(N):
    for _ in range(i):
        print("  ", end='')
    
    for _ in range(2*(N-i)-1):
        print("* ", end='')
    print()

