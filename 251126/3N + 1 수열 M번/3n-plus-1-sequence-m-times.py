import sys

m = int(input())
arr = list(map(int, sys.stdin.read().split()))
s = 0

for i in range(m):
    while arr[i] != 1:
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
            s += 1
        else:
            arr[i] = arr[i] * 3 + 1
            s += 1
    print(s)
    s = 0
