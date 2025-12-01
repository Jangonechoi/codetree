import sys

a = list(map(int, sys.stdin.read().split()))
row = a[0]
column = a[1]
arr = [[0 for _ in range(column)] for _ in range(row)]
num = 1
for i in range(row):
    for j in range(column):
        arr[i][j] = num
        num += 1

for abc in arr:
    for elem in abc:
        print(elem, end=' ')
    print()