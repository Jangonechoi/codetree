import sys

arr = list(map(int, sys.stdin.read().split()))

if 999 in arr:
    print(max(arr[:arr.index(999)]), min(arr[:arr.index(999)]))
elif -999 in arr:
    print(max(arr[:arr.index(-999)]), min(arr[:arr.index(-999)]))
