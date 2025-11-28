import sys

arr = list(map(int, sys.stdin.read().split()))
# print(arr)
arr2 = []
for i in range(len(arr)):
    if arr[i] != 0:
        arr2.append(str(arr[i]))
    else:
        break
arr2.reverse()
print(' '.join(arr2))
    