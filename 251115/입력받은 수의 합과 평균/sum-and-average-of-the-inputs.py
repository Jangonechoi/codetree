import sys

a = list(map(int, sys.stdin.read().split()))

s = sum(a) - a[0]
avg = s/(len(a)-1)

print(s, avg)