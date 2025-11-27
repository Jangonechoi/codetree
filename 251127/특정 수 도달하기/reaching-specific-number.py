import sys

arr = list(map(int, sys.stdin.read().split()))
# print(arr)
a = []
for i in range(len(arr)):
    if arr[i] < 250:
        a.append(arr[i])
    elif arr[i] >= 250:
        break
s = sum(a)
avg = sum(a) / len(a)
print(f"{s} {avg:.1f}")
