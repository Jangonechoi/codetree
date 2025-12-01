import sys

arr = list(map(int, sys.stdin.read().split()))
arr2 = []
arr3 = []

for i in range(len(arr)):
    if arr[i] < 500:
        arr2.append(arr[i])
    else:
        arr3.append(arr[i])
print(max(arr2), min(arr3))


