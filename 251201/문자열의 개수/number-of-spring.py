import sys

arr = list(filter(lambda x : x != '0', sys.stdin.read().split()))

print(len(arr))
for i in range(len(arr)):
    if i % 2 == 0:
        print(arr[i])
    