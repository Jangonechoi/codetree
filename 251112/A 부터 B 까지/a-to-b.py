arr = list(map(int,input().split()))
a,b = arr[0],arr[1]
s = ''

while(a <= b):
    s += str(a) + ' '
    if a % 2 == 0:
        a += 3
    else:
        a += a
print(s)
