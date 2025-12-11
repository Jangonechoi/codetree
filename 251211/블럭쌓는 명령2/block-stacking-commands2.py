n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
# print(n, k) => 7 4
# print(commands) => [(5, 5), (2, 4), (4, 6), (3, 5)]
arr = [ 0 for x in range(n)]
# => [0, 0, 0, 0, 0, 0, 0]
# print(arr)
for i in range(len(commands)):
    for j in range(commands[i][-1] - commands[i][0] + 1):
        arr[commands[i][0] + j -1] += 1
print(max(arr))
    


