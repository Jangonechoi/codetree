import sys

nums = list(map(int, sys.stdin.read().split()))
arr = len([x for x in nums if x % 2 == 0])

print(arr)