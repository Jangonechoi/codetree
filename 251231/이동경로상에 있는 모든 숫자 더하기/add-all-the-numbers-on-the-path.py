N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

# N은 항상 홀수로 주어짐
# 시작위치 좌표(정중앙)
x, y = (N - 1) // 2, (N - 1) // 2
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
curr_dir = 0
total_sum = board[x][y]

def can_move(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for cmd in commands:
    if cmd == 'R':
        curr_dir = (curr_dir + 1) % 4
    elif cmd == 'L':
        curr_dir = (curr_dir - 1) % 4
    elif cmd == 'F':
        nx, ny = x + dxs[curr_dir], y + dys[curr_dir]
        if can_move(nx,ny):
            x, y = nx, ny
            total_sum += board[x][y]

print(total_sum)


