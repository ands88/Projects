# https://youtu.be/jCzT9XFZ5bw?si=NpCuNX_45RXBWqeY
# Decorators - Quando precisamos mudar um atributo de uma classe, sem precisar modificar todo o código, usamos getter e setter.

class Employee:
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @property #colocando o @property podemos acessar o método email como se fosse um atributo.
    def email(self):
        return '{}.{}@company.com'.format(self.first_name, self.last_name)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name


    @fullname.deleter
    def fullname(self):
       print('Delete name!')
       self.first_name = None
       self.last_name = None


emp_1 = Employee('Anderson', 'Martins', 80000)

emp_1.fullname = 'Johan Schmidt'

print(emp_1.first_name)
print(emp_1.email)
print(emp_1.pay)
print(emp_1.fullname)

del emp_1.fullname