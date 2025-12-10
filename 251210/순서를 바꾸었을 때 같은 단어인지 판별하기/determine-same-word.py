word1 = input()
word2 = input()

# Please write your code here.
word1 = [x for x in word1]
word2 = [x for x in word2]
word1.sort()
word2.sort()
print('Yes') if word1 == word2 else print('No')
