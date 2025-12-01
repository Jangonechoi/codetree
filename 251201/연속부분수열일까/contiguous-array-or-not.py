import sys
N = list(map(int, sys.stdin.read().split()))
arr1 = N[2:N[0]+2]
arr2 = N[N[0]+2:]
m = len(arr1)
s = len(arr2)

def is_subsequence(arr1, arr2):
    if s > m:
        return('No')
    for i in range(m - s +1):
        current_slice = arr1[i : i + s]
        if current_slice == arr2:
            return('Yes')
    return 'No'

result = is_subsequence(arr1, arr2)
print(result)










# 처음 시도했던 풀이
# for i in range(len(arr1)):
#     # arr1을 돌면서 arr2와 같을 경우에만 val_arr채우기 진행
#     if arr1[i] == arr2[c]:
#         # arr2의 길이만큼 반복
#         for j in range(len(arr2)):
#             # arr2와 arr1이 일치하면 val_arr에 append 시작
#             if arr2[j] == arr1[i]:
#                 val_arr.append(arr1[i])
#             # 다를 경우에는 문자0을 채워서 일치하지 않게 만듬
#             if arr2[j] != arr1[i]:
#                 val_arr.append('0')
#             # val_arr가 더 길어지면('0'이추가되어서 어차피 일치하지 않으므로) 배열을 초기화
#             if len(val_arr) > len(arr2):
#                 val_arr = []
#             # 배열이 일치하면 'Yes'출력 후 종료
#             if val_arr == arr2:
#                 print('Yes')
#                 break
#         # c += 1
# print(val_arr)
