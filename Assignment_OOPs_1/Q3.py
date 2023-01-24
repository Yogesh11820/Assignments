class Age_check(Exception):
    pass

def user_data(age):
    if age < 18:
        raise Age_check("Your not allowed for vote")
    else:
        print("Your allowed to vote")

try:
    age = int(input("Enter your age: "))
    user_data(age)
except Age_check as e:
    print(e)
