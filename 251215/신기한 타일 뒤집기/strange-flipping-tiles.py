n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.
# print(n, commands, x, dir) => 4 [('4', 'R'), ('5', 'L'), ('7', 'R'), ('4', 'L')] [4, 5, 7, 4] ['R', 'L', 'R', 'L']
arr = [0] * 200001 
offset = 100000
current_pos = offset

for i in range(n):
    # 이동할 거리 설정
    distance = x[i]
    if dir[i] == 'R':
        for j in range(current_pos, current_pos + distance):
            arr[j] = 1
        # print(arr[99990:100010])
        current_pos += distance
    else:
        for j in range(current_pos - distance, current_pos):
            arr[j] = -1
        # print(arr[99990:100010])
        current_pos -= distance

print(arr.count(-1), arr.count(1))