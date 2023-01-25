class Loan_chk(Exception):
    pass

class Person:
    def __init__(self, salary):
        self.salary = salary
    
    def chk_status(self):
        if self.salary < 10000:
            raise Loan_chk("Not eligible")
        else:
            return 'your eligible'

try:
    salary = int(input("Enter your salary: "))
    person = Person(salary)
    print(person.chk_status())
except Loan_chk as e:
    print(e)
