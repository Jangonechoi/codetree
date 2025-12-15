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
        for j in range(distance):
            arr[current_pos + j] = -1
        current_pos += distance -1
    else:
        for j in range(distance):
            arr[current_pos - j] = 1
        current_pos -= distance -1
print(arr.count(1), arr.count(-1))