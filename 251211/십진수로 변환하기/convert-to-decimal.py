binary = list(map(int, input()))

# Please write your code here.
# print(binary)
s = 0
for i in range(len(binary)-1):
    s += binary[i]*2**(len(binary)-i-1)
s += binary[-1]
print(s)