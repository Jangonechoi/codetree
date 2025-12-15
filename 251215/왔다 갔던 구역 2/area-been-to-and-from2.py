n = int(input())
x = []
direction = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    direction.append(di)

# print(n, x, direction) 6 [2, 6, 1, 8, 1, 2] ['R', 'L', 'R', 'L', 'R', 'R']
arr = [0] * 2001
offset = 1000
current_pos = offset

for i in range(n):
    distance = x[i]
    if direction[i] == 'R':
        for j in range(current_pos, current_pos + distance):
            arr[j] += 1
        current_pos += distance
    else:
        for j in range(current_pos - distance, current_pos):
            arr[j] += 1
        current_pos -= distance

arr = list(filter(lambda x : x > 1, arr))
print(len(arr))
