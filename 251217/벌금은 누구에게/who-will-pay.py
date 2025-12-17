N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.
# print(N, M, K, student) 5 7 3 [2, 5, 2, 3, 5, 2, 4]
arr = [0] * (N+1)

for i in range(M):
    arr[student[i]] += 1
    if K in arr:
        break

if K in arr:
    print(arr.index(K))
else:
    print(-1)



