import sys

n, t = map(int, input().split())
arr = list(filter(lambda x : x > t, map(int, sys.stdin.read().split())))

# Please write your code here.
# print(n, t, arr) 7 3 [6, 7, 8, 4, 5]
maxlen = 1
cnt = 1
if len(arr) == 0 or len(arr) == 1:
    print(len(arr))
else:
    for i in range(1,len(arr)):
        if arr[i-1] < arr[i]:
            cnt += 1
        else:
            if maxlen < cnt:
                maxlen = cnt
            cnt = 1
    if maxlen < cnt:
        maxlen = cnt
print(maxlen)