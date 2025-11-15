import sys

arr = list(map(int, sys.stdin.read().split()))
S = 0

for i in range(arr[0], arr[1]+1):
    if 1920 % i == 0 and 2880 % i == 0:
        S = 1
        break
print(S)