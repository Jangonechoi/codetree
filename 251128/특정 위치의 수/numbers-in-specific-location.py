import sys

arr = list(map(int, sys.stdin.read().split()))
s = 0
for i in range(10):
    a = arr[i]
    if i == 2 or i == 4 or i == 9:
        s += a
print(s)