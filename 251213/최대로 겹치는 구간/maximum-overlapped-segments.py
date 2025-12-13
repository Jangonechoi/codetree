n = int(input())
segments = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 길이 200 배열생성(OFFSET 100 더해줬을 경우 상정)
arr = [0 for x in range(200)]

# n번 반복으로 구간에 1씩 값 더한 후 n값 count로 겹치는 구간 찾기
# print(len(arr[segments[0][0]:segments[0][1]])) : 더해줄 구간의 길이
# 음수일 경우 대비해서 OFFSET 더하기
for i in range(n):
    for j in range(2):
        segments[i][j] += 100
# 구간 채우기
for i in range(n):
    for j in range(len(arr[segments[i][0]:segments[i][-1]])):
        arr[segments[i][0]+j] += 1
print(max(arr))
