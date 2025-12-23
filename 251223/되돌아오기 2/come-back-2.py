import sys
commands = input()

# Please write your code here.
commands = [commands[x] for x in range(len(commands))]
# ['F', 'F', 'F', 'R', 'F', 'F', 'R', 'F', 'F', 'F', 'R', 'F', 'F', 'F', 'F', 'F', 'F']

x, y = 0,0
elapsed_time = 0
ans = -1
xds, yds = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0

for i in range(len(commands)):
    # 초기 방향은 북쪽(0,1)
    nx, ny = xds[dir_num], yds[dir_num]
    # f일때는 현재 방향으로 전진
    if commands[i] == 'F':
        x, y = x + nx , y + ny
        elapsed_time += 1
    elif commands[i] == 'R':
        dir_num = (dir_num + 1) % 4
        elapsed_time += 1
    elif commands == 'L':
        dir_num = (dir_num + 3) % 4
        elapsed_time += 1

    if x == 0 and y == 0:
        ans = elapsed_time
        break
# print(elapsed_time)
print(ans)