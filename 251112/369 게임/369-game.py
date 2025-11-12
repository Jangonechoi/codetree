a = int(input())
b = []
i = 1

while i <= a:
    if i % 3 == 0 or '3' in str(i) or '6' in str(i) or '9' in str(i):
        b.append('0')
    else:
        b.append(str(i))
    i += 1
print(' '.join(b))


