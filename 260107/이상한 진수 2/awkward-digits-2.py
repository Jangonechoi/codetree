a = list(map(int, input()))

# Please write your code here.

if 0 in a:
    a[a.index(0)] = 1
else:
    a[-1] = 0

a2 = a[::-1]
s = 0
for i in range(len(a2)):
    if a2[i] == 1:
        s += a2[i] * 2**i
print(s)


