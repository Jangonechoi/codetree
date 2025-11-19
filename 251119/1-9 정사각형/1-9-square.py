import sys

N = int(sys.stdin.read())
# print(N)
cnt = 1

for i in range(N):
    for j in range(N):
        print(cnt,end='')
        cnt += 1
        if cnt == 10:
            cnt = 1
    print()
    