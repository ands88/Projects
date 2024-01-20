# https://youtu.be/u-OmVr_fT4s?si=cVNeKLo6NN1QXLjx
# Parametro é o que colocamos dentro da função, por exempolo - def greet (first_name, last_name) - first name e last name são os parâmetros
# Argumento é o valor que damos para o parâmetro

def greet (first_name, last_name):
    print (f'Hi {first_name} {last_name}')
    print ('Welcom aboard\n')

greet ('Anderson', 'Martins')
greet ('Neuber', 'de Castro')


# Temos dois tipos de funções:
# 1 - Faz uma tarefa
# 2 - Calcula e retorna um valor
def get_greeting (name):
    return f'Hi, {name}'

message = get_greeting('Anderson')
print(message)
with open('content.txt', 'w') as file:
    file.write(message)


# increment keyword
def increment (number, by):
    return number + by

add1 = increment (5, 3)

print (add1)

print(increment(10,by=5))


#deafult argument
def increment (number, by=5): # nesse caso, o valor padrão será 5, caso o usuário não coloque nenhum argumento, será usado o padrão. Todos os parâmetros opcionais devem ser colocados por último
    return number + by

print(increment(10))
print(increment(5, 3))

# *args - o *args pode ser usado como uma variável, pode dar o nome que preferir
def multiply (*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply (2, 3, 4, 5, 6))

# **args
def save_user(**user):
    print(user)

save_user(id=1, name='Anderson', age='35')
