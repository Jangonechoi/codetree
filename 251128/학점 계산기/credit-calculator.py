import sys

n = int(input())
arr = list(map(float, sys.stdin.read().split()))

# print(n, arr) => 4.0 [3.0, 2.8, 4.0, 3.5]
avg = sum(arr) / len(arr)
print(f'{avg:.1f}')

if avg >= 4:
    print('Perfect')
elif 3 <= avg  < 4:
    print('Good')
else:
    print('Poor') 