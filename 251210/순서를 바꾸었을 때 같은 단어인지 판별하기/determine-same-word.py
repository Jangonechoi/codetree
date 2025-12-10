word1 = input()
word2 = input()

# Please write your code here.
# print(word1, word2)
if len(word1) == len(word2) and len(set(word1) & set(word2)) == len(set(word1)):
    print('Yes')
else:
    print('No')