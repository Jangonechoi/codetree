import sys
N = input().split()
# print(N)
arr = list(map(int, sys.stdin.read().split()))
print(arr.count(int(N[1])))

