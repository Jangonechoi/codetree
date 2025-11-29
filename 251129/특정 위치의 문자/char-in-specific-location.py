import sys

arr = ['L', 'E', 'B', 'R', 'O', 'S']

N = str(input())
# print(N)
if N in arr:
    print(arr.index(N))
else:
    print('None')