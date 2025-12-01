import sys

n = 4
arr2 = []
for _ in range(n):
    arr = list(map(int, input().split()))
    arr2.append(arr)

for i in range(n):
    print(sum(arr2[i]))