# https://youtu.be/3ohzBxoFHAY?si=wubTkzZDIJvS7ucV
# magic methods / dunder methods
# repr - representação "inambígua" do objeto e deve ser usada para debugging, logging
# str - readable representation of an object. Usada para o usuário

class Employee:
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@'+'company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first_name, self.last_name, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())
emp_1 = Employee('Anderson', 'Martins', 80000)
emp_2 = Employee('Test', 'User', 70000)


print(emp_1 + emp_2)

print(len(emp_1))
""" print(emp_1)

print(repr(emp_1)) 
print(str(emp_1)) """

