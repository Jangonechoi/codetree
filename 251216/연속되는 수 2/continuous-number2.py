n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# print(n, arr)
count = 1
MaxCount = 1

if n == 1:
    print(MaxCount)
else:
    for i in range(1,n):
        if arr[i-1] == arr[i]:
            count += 1
        elif MaxCount < count:
            MaxCount = count
            count = 1
    print(MaxCount)