import sys

n, t = map(int, input().split())
original_arr = list(map(int, sys.stdin.read().split()))

# Please write your code here.
# print(n, t, arr) 7 3 [6, 7, 8, 4, 5]
maxlen = 0
cnt = 0

for i in range(n):
    if original_arr[i] > t:
        cnt += 1
    else:
        if maxlen < cnt:
            maxlen = cnt
        cnt = 0
if maxlen < cnt:
    maxlen = cnt
print(maxlen)