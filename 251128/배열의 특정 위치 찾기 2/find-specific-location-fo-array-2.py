import sys

arr = list(map(int, sys.stdin.read().split()))
arr1 = []
arr2 = []

for i in range(1,len(arr)+1):
    if i % 2 != 0:
        arr1.append(arr[i-1])
    else:
        arr2.append(arr[i-1])

s1 = sum(arr1)
s2 = sum(arr2)

if s1 > s2:
    print(s1-s2)
elif s2 > s1:
    print(s2-s1)
else:
    print(0)
    