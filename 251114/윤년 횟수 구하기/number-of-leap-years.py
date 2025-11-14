N = int(input())
s = 0

for i in range(1, N):
    if i % 4 == 0:
        s += 1
        if (i % 100 == 0) and (i % 400 != 0):
            s += -1 
print(s)
