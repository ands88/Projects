# se o valor for divisivel por 3, retorna fizz, se for divisivel por 5, retorna buzz. Se for divisivel por 3 E 5, retorna fizz_buzz. Para qualquer outro número, retorna o próprio número

def fizz_buzz(input):
    if input %3 == 0 and input %5 ==0:
        return 'FizzBuzz'
    elif input %5 == 0:
        return 'Buzz'
    elif input %3 == 0:
        return 'Fizz'
    else:
        return input

print (fizz_buzz(5))

