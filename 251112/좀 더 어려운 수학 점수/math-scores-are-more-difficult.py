arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
# print(arr1,arr2)

if arr1[0] > arr2[0]:
    print('A')
elif arr2[0] > arr1[0]:
    print('B')
elif arr1[0] == arr2[0] and arr1[1] > arr2[1]:
    print('A')
elif arr1[0] == arr2[0] and arr2[1] > arr1[1]:
    print('B')
