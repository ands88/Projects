# https://youtu.be/ZDa-Z5JzLYM?si=F02VhLSX0M48ChHt
# as classes permitem agrupar logicamente os dados e as funções de um modo que seja fácil de usá-los novamente
# assim como construir em torno deles se preciso for
# uma classe é uma planta para contruir instâncias
import datetime

class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@'+'company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, pay = emp_str.split('-')
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Anderson', 'Martins', 80000)
emp_2 = Employee('Test', ' User', 70000)


""" print(emp_1.email)
print(emp_2.email)
print('{} {}'.format(emp_1.first_name, emp_1.last_name))

print(emp_1.fullname()) # similar a Employee.fullname(emp_1)
print(emp_2.fullname()) """
# https://youtu.be/BJ-VvGyQxho?si=EHU0fut27eNIHQIC - class variables
# variável de classe é uma variável compartilhada por todas as instâncias de uma classe.

""" emp_1.raise_amt = 1.05
emp_2.raise_amt = 1.03 """

""" print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)

Employee.set_raise_amt(1.10)

print(Employee.raise_amt)
print('Emp 1', emp_1.raise_amt)
print('Emp 2', emp_2.raise_amt)

print(Employee.num_of_emps)
 """
# https://youtu.be/rq8cL2XMM5M?si=DWxAeG7YZMF9LhZN
# classmethod e staticmethod

emp_str1 = "John-Doe-70000"
emp_str2 = "Anderson-Martins-40000"
emp_str3 = "Clara-Who-90000"

new_emp_1 = Employee.from_string(emp_str1)
new_emp_2 = Employee.from_string(emp_str2)
new_emp_3 = Employee.from_string(emp_str3)

print(new_emp_1.email)
print(new_emp_1.pay)

my_date = datetime.date(2024, 1, 27)

print(Employee.is_workday(my_date))