n, m = map(int, input().split())
if n == m:
    print(n)
# 두 수의 곱: 최소공배수x최대공약수
# 12*18 = 6*36 = 216
a = n*m
b = 0
if n > m:
    for i in range(-m,-(m // 2)+1):
        if m % -i == 0 and n % -i == 0:
            b = -i
            break
else:
    for i in range(-n,-(n // 2)+1):
        if n % -i == 0 and m % -i == 0:
            b = -i
            break
print(a//b)

