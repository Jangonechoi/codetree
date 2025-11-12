arr = input().split()
h = int(arr[0])
w = int(arr[1])
b = int(w // (h/100)**2)

if b >= 25:
    print(f"{b}\nObesity")
else:
    print(b)
