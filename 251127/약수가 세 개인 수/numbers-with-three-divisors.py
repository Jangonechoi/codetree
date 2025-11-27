import sys
start, end = map(int, sys.stdin.read().split())
# print(start,end)
c = 0
for i in range(start,end+1):
    s = 0
    for j in range(1,i+1):
        if i % j == 0:
            s += 1
    if s == 3:
        c += 1
print(c)


