# Get the elements from position a to position b from list

def printno(list,a,b):
   print(list[a:b])

list = [1,2,3,4,5,6]
a = int(input("Enter the starting position: "))
b = int(input("Enter the last position: "))

printno(list,a-1,b)