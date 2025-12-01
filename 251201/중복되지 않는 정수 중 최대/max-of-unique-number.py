import sys
n = int(input())
nums = list(map(int, sys.stdin.read().split()))
arr = []
# print(n, nums)
for i in range(len(nums)):
    if nums.count(nums[i]) == 1:
        arr.append(nums[i])
    
if len(arr) == 0:
    print(-1)
else:
    print(max(arr))