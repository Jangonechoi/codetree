n = int(input())
arr = []

while True:
    if n < 2:
        arr.append(str(n))
        break
    arr.append(str(n % 2))
    n //= 2

arr = ''.join(arr[::-1])
print(arr)
