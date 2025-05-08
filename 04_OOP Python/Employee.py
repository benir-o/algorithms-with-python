# Employee class
import datetime
my_date=datetime.date(2005,11,17)
class Employee:
    num_of_emps=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        Employee.num_of_emps+=1

    def fullname(self):
        return "{} {}".format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    #alternative constructor
    #static methods don't pass anything automatically, as shown below
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


emp_1=Employee('Benir','Odeny',60000)
emp_2=Employee('Test','User',50000)
print(emp_1.fullname())
print(emp_2.fullname())
# class variables - shared among all instances of a class

print(Employee.num_of_emps)
Employee.set_raise_amt(1.06)
print(Employee.raise_amount)


emp_3_str="John-Doe-5000"
emp_4_str="Alisson-Becker-60000"

print(Employee.is_workday(my_date))



