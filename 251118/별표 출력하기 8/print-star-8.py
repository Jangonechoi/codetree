import sys

N = int(sys.stdin.read())
# print(N)
for i in range(1,N+1):
    if i % 2 == 0:
        print('* '* i)
    else:
        print('*')


