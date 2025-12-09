n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
# print(arr) [6, 5, 4, 3, 2, 1]
# print(queries) [(1, 2), (2, 4), (3, 4), (5, 6)]
# queries[0] (1, 2)
def sectionSum():
    for i in range(m):
        s = 0
        s = sum(arr[queries[i][0]-1:queries[i][1]])
        print(s)

sectionSum()



