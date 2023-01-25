def divide_num(*args):
    for i in range(0,4):
        try:
           ans = args[i][0]/args[i][1]
           print(ans)
        except ZeroDivisionError:
           print("Error: Denominator cannot be 0.")
        except TypeError:
           print("Error: Denominator cannot be character.")

    
divide_num((1,0),(1,2),(6,3),(1,'a'))