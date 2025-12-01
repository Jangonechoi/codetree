import sys
n = int(input())
arr = list(map(int, sys.stdin.read().split()))

# print(n, a)

# print(arr.index(m))
for i in range(len(arr)):
    m = max(arr)
    print(arr.index(m)+1,end=' ')
    arr = arr[:arr.index(m)]
    if len(arr) < 1:
        break


