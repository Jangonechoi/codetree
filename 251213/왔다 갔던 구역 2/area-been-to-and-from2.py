n = int(input())
x = []
direction = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    direction.append(di)

# Please write your code here.
# print(n, x, direction) 6 [2, 6, 1, 8, 1, 2] ['R', 'L', 'R', 'L', 'R', 'R']
arr = [0] * 2000
start = 999
for i in range(n):
    if direction[i] == 'R':
        for j in range(x[i]):
            arr[start + j] += 1
        start += x[i]
    else:
        for j in range(x[i]):
            arr[start - j] += 1
        start -= x[i]
arr = list(filter(lambda x : x > 1, arr))
print(len(arr))
        

