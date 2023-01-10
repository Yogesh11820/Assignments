# Check if string contains repeated characters

def checkit(s):
    char_freq = {}
    for i in s:
      if i in char_freq:
        char_freq[i] += 1
      else:
        char_freq[i] = 1

    for freq in char_freq.values():
        if(freq>1):
            return True
    return False

s = input("Enter the string : ")
checkit(s)

if(checkit(s)):
    print("String contain repeated characters")
else:
    print("String not contain repeated characters")
