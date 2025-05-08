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
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{}-->{}'.format(self.fullname(),self.email)
    def __add__(self, other):
        return self.pay +other.pay
    def __len__(self):
        return len(self.fullname())

# What is a dunder method

#Method Resolution order
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees= employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->',emp.fullname())









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

dev_1=Developer('Merlin','Haven',379400,'Python')
dev_2=Developer('Jayesh','Menariya',57300,'Java')
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_1.pay)

mgr_1=Manager('Reyna','Giovanni',900000,[dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
#--> is instance
print(isinstance(mgr_1, Manager))
print(issubclass(Developer,Employee))
print(emp_1)
# Question-> What if we want to create a method that adds the salaries of all employees
# all together?
print(emp_1+emp_2)
print(len(emp_1))