import sys

dirs = [x for x in input()]

# Please write your code here.
xd, yd = [0, -1, 0, 1], [1, 0, -1, 0]
x, y = 0, 0
dir_num = 0
for i in range(len(dirs)):
    if dirs[i] == 'L':
        dir_num = (dir_num+1) % 4
    elif dirs[i] == 'R':
        dir_num = (dir_num+3) % 4
    elif dirs[i] == 'F':
        x, y = x + xd[dir_num], y + yd[dir_num]
print(x, y)