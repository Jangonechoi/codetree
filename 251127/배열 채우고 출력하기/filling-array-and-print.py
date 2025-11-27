import sys

arr = list(map(str, sys.stdin.read().split()))
arr.reverse()
print(''.join(arr))