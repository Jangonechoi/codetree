import sys

arr = list(map(int, sys.stdin.read().split()))
# print(arr)
s = 0
s2 = 0
s2_len = 0

for i in range(1,len(arr)+1):
    if i % 2 == 0:
        s += arr[i-1]
        # print(arr[i-1])
    if i % 3 == 0:
        s2 += arr[i-1]
        s2_len += 1
        # print(arr[i-1])
avg = s2 / s2_len
print(f'{s} {avg:.1f}')
