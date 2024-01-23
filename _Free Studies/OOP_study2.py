# https://youtu.be/RSl87lqOXDE?si=WImWhuUTtymE7KG1
# Inheritance - Creating subclasses - Herança permite herdar métodos e atributos de uma outra classe pai
# MRO - Method Resolution Order - Ordem de resolução dos métodos dentro de uma superclasse e uma subclasse

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


class Developer (Employee):
    raise_amt = 1.10 # ao criar a variável na subclasse, nada é mudado na super classe, tornando aquela variável específica para a subclasse.
    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang


class Manager (Employee):
    def __init__(self, first_name, last_name, pay, employees = None):
        super().__init__(first_name, last_name, pay)
        self.employees = employees
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_employees (self):
        for emp in self.employees:
            print('-->', emp.fullname())
    



dev_1 = Developer('Anderson', 'Martins', 80000, 'Python')
dev_2 = Developer('Test', 'User', 70000, 'Javascript')


manager1 = Manager('Neuber', 'Castro', 150000, [dev_1])
manager2 = Manager('Test', 'Manager', 150000, 'Test User')


print(isinstance(manager1, Employee))
print(issubclass(Manager, Developer))


# print(manager1.email)

# manager1.add_employee(dev_2)

# manager1.print_employees()

# manager1.remove_employee(dev_2)

# manager1.print_employees()


# print(help(Developer))

# print (dev_1.email)
# print (dev_2.email)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.email)
# print(dev_1.prog_lang)