def divide_num(*args):
    try:
        ans = args[0]/args[1]
        print(ans)
    except ZeroDivisionError:
        print("Error: Denominator cannot be 0.")
    except TypeError:
        print("Error: Denominator cannot be character.")

    
divide_num(1,0)