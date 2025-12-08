import sys
a, b = map(int, sys.stdin.read().split())

def solution(x,y):
    if x < y:
        return f"{min(x,y)*2} {max(x,y)+25}"
    else:
        return f"{max(x,y)+25} {min(x,y)*2}"
print(solution(a,b))
