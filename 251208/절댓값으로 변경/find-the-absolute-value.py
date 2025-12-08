import sys
n = int(input())
arr = list(map(lambda x : str(abs(x)), map(int, sys.stdin.read().split())))
print(' '.join(arr))



