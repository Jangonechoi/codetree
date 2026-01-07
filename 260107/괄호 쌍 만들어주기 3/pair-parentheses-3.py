A = input()

# Please write your code here.

answer = '()'
cnt = 0

for i in range(len(A)):
    for j in range(1,len(A)-i):
        if A[i] + A[i+j] == answer:
            cnt += 1
print(cnt)

