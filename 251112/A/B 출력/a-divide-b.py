arr = list(map(float,input().split()))
a = arr[0]
b = arr[1]
c = 0
d = 0
for i in range(0,21):
    c += (a // b)
    d = (a % b) // b
    i += 1

