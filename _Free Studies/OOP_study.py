# https://youtu.be/ZDa-Z5JzLYM?si=F02VhLSX0M48ChHt
# as classes permitem agrupar logicamente os dados e as funções de um modo que seja fácil de usá-los novamente
# assim como construir em torno deles se preciso for
# uma classe é uma planta para contruir instâncias

class Employee:
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@'+'company.com'

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amount)

emp_1 = Employee('Anderson', 'Martins', 80000)
                 
print(emp_1.email)

print('{} {}'.format(emp_1.first_name, emp_1.last_name))

print(emp_1.fullname()) # similar a Employee.fullname(emp_1)

# https://youtu.be/BJ-VvGyQxho?si=EHU0fut27eNIHQIC - class variables
# variável de classe é uma variável compartilhada por todas as instâncias de uma classe.

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)