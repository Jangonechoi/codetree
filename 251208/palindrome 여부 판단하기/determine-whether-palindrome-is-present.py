A = input()

def isPalindrome(a):
    if A == A[::-1]: 
        return 'Yes'
    else:
        return 'No'
print(isPalindrome(A))
