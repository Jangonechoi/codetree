import sys
n = int(input())
a = list(map(int, sys.stdin.read().split()))

# print(n, a)
a.sort(reverse = True)
print(a[0],a[1])

