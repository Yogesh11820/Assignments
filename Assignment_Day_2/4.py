def Add(num1,num2):
    print("Addition of num1 & num2 is: ",num1+num2)
def Sub(num1,num2):
    print("Subtraction of num1 & num2 is: ",num1-num2)
def Mul(num1,num2):
    print("Addition of num1 & num2 is: ",num1*num2)
def Div(num1,num2):
    print("Addition of num1 & num2 is: ",num1/num2)

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

s = input("Enter the operation: ")
if(s=='Add'):
    Add(num1,num2)
elif(s=='Subtract'):
    Sub(num1,num2)
elif(s=="Multiply"):
    Mul(num1,num2)
elif(s=="Division"):
    Div(num1,num2)
