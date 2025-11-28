import sys

arr = list(map(float, sys.stdin.read().split()))
print(sum(arr)/ len(arr))