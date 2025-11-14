import sys

N = int(sys.stdin.read())

s = [x for x in range(N)]

s = list(filter(lambda x : (N % (x+1) == 0), s))

if N == sum(s) + len(s) - N:
    print('P')
else:
    print('N')


