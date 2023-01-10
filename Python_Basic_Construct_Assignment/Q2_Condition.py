# Check if string palindrome or not 

def checkpalindrome(s):
    for i in range(0,int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

s = input("Enter the String : ")
checkpalindrome(s)

if(checkpalindrome(s)):
    print("String is palindrome")
else:
    print("string is not palindrome")
