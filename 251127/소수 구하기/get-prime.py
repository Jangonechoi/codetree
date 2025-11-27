import sys

n = int(sys.stdin.read())
# print(n)
if n == 1:
    print(1)

sieve = [True] * (n+1)
answer = ''
m = int(n**0.5)
for i in range(2,m+1):
    if sieve[i] == True:
        for j in range(i+i, n+1, i):
            sieve[j] = False
for i in range(2, n+1):
    if sieve[i] == True:
        answer += str(i)+' '
print(answer)