n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
nums2 = list(reversed(nums))
arr = [str(x) for x in nums]
arr2 = [str(x) for x in nums2]

print(' '.join(arr))
print(' '.join(arr2))