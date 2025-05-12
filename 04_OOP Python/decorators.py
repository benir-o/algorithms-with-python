class Employee:
    raise_amt=1.05
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    @property
    def email(self):
        return "{}{}@gmail.com".format(self.first,self.last).lower()
    # We have defined our email as a method, and we can be able to
    # access it like an attribute

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first, last=name.split(' ')
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print("Delete Name")
        self.first=None
        self.last=None


emp_5=Employee('Benir','Odeny',50000)
emp_5.fullname='Corey Shafer'
print(emp_5.first)
print(emp_5.email)
print(emp_5.fullname)
print("Initial commit")

del emp_5.fullname
