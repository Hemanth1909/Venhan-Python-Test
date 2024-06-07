def is_palindrome(s):
    rev = ""
    for i in range(len(s), 0, -1):
        rev += s[i-1]
    
    # print(rev)
    if(rev == s):
        return True
    else:
        return False

print(is_palindrome("Hemanth"))
print(is_palindrome("madam"))
