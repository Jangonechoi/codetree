n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
# print(n, arr)
count = 0
MaxCount = 0

for i in range(n-1):
    if i == 0 or arr[i] == arr[i+1]:
        count += 1
    elif MaxCount < count:
        MaxCount = count
        count = 0
print(MaxCount)