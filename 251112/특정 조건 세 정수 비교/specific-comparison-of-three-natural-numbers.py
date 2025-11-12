arr = list(map(int, input().split()))
m = min(arr)

if arr.count(arr[0]) == 3:
    print(1,1)
elif arr[0] == m:
    print(1,0)
else:
    print(0,0)
