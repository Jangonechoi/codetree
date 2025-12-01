import sys

n = int(input())
arr = list(map(int, sys.stdin.read().split()))
# print(n,arr)
m = min(arr)
print(m,arr.count(m))


