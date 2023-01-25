# Replace the digits from string inside list

list = ['name512','same1example','joy18full']
p = 0
for str in list:                                   # Access the element of list one by one 
    new_str = ''                                   
    for ch in str:                                 # Access the character of that element to check whether its digit or not
        if(ch>='a' and ch<='z'):
            new_str+=ch
    list[p] = new_str
    p+=1
print(list)