import sys

arr = list(map(int, sys.stdin.read().split()))
# print(arr)
arr1 = list(filter(lambda x : x % 2 == 0 , arr))
arr2 = list(filter(lambda x : x % 3 == 0, arr))
arr2_avg = sum(arr2) / len(arr2)
print(f"{sum(arr1)} {arr2_avg:.1f}")
