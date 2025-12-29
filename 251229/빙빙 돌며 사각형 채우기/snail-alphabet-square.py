n, m = map(int, input().split())

# Please write your code here.
# chr(65) ~ chr(90)
# arr = [x + 65 for x in range(26)]
# => [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]

answer = [
    [0] * m
    for _ in range(n)
]

def canMove(x, y):
    return 0 <= x < n and 0 <= y < m and answer[x][y] == 0

xds, yds = [0, 1, 0, -1], [1, 0, -1, 0]
dir_num = 0
x,y = 0,0

a = 65
answer[x][y] = chr(a)

for i in range(n * m):
    answer[x][y] = chr(65 + (i % 26))

    if i == n * m -1:
        break

    nx, ny = x + xds[dir_num], y + yds[dir_num]

    if not canMove(nx, ny):
        dir_num = (dir_num + 1) % 4
        nx, ny = x + xds[dir_num], y + yds[dir_num]

    x, y = nx, ny

for row in answer:
    print(*(row))






