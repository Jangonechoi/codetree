import sys

n = int(input())
# print(n)
# arr = list(map(int, sys.stdin.read().split()))
# print(arr) [1, 10, 1, 20, 5, 30]

for _ in range(n):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    s = 0
    for i in range(a,b+1):
        if i % 2 == 0:
            s += i
    print(s)









