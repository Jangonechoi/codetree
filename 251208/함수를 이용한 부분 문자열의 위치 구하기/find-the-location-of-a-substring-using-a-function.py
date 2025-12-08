text = input()
pattern = input()

def solution():
    if pattern in text:
        return(text.index(f'{pattern}'))
    else:
        return -1
print(solution())