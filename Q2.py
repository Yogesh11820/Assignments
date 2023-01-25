# filter digits and alphabets separately

list_1 = [1,'a',2,'b',3,'c']
ans = filter(lambda ch: type(ch)==type('') , list_1)    # Check the type of character if its a string then it will add in list_1
print(list(ans))
ans = filter(lambda ch: type(ch)==type(0) , list_1)     # Check the type of character if its a number then it will add in list_2
print(list(ans))


