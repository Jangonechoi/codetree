import sys

start, end = map(int, sys.stdin.read().split())
count = 0
s = 0
# print(start, end)

for i in range(start,end):
    for j in range(1,i):
        if i % j == 0:
            s += j
    if i == s:
        count += 1
    s = 0
print(count)    