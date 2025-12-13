n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

# print(n, segments) => 3 [[1, 5], [4, 6], [2, 4]]
# 최대길이의 배열 생성
arr = [0 for x in range(101)]
# print(len(arr[segments[0][0]:segments[0][-1]])+1)
for i in range(n):
    for j in range(len(arr[segments[i][0]:segments[i][-1]])+1):
        arr[segments[i][0]+j] += 1
print(max(arr))
