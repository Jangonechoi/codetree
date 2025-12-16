x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

max_r = 2001
offset = 1000

checked = [
    [0] * max_r
    for _ in range(max_r)
]

# offset 더해주기
for i in range(3):
    x1[i] += offset
    y1[i] += offset
    x2[i] += offset
    y2[i] += offset

for i in range(3):
    if i == 2:
        for x in range(x1[i],x2[i]):
            for y in range(y1[i],y2[i]):
                checked[x][y] = 0
    else:
        for x in range(x1[i],x2[i]):
            for y in range(y1[i],y2[i]):
                checked[x][y] = 1
area = 0
for x in range(0, max_r):
    for y in range(0, max_r):
        if checked[x][y] == 1:
            area += 1
print(area)

