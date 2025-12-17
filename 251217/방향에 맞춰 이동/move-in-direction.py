import sys

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
# print(n, moves, dir, dist) => 4 [('N', '3'), ('E', '2'), ('S', '1'), ('E', '2')] ['N', 'E', 'S', 'E'] [3, 2, 1, 2]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x, y = 0, 0
for i in range(n):
    if dir[i] == 'E':
        x = x + dx[0]*dist[i]
    elif dir[i] == 'S':
        y = y + dy[1]*dist[i]
    elif dir[i] == 'W':
        x = x + dx[2]*dist[i]
    elif dir[i] == 'N':
        y = y + dy[3]*dist[i]
sys.stdout.write(str(x) +' '+ str(y))
