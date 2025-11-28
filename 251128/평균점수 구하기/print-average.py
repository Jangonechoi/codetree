import sys

arr = list(map(float, sys.stdin.read().split()))
print(f"{sum(arr)/ len(arr):.1f}")