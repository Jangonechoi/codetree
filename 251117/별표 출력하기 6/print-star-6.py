import sys

N = int(sys.stdin.read())
# print(N)
cnt = 0

for i in range(N):
    for _ in range(cnt):
        print('  ', end='')
    cnt += 1
    for _ in range(2*(N-i)-1):
        print("* ", end='')
    print()
cnt = N-2

for i in range(N-1):
    for _ in range(cnt):
        print('  ', end='')
    cnt -= 1
    for _ in range(2*(2+i)-1):
        print("* ", end='')
    print()




