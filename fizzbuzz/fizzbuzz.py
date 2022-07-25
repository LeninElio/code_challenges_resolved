"""

Escribir un programa que muestre en pantalla los números del 1 al 100, sustituyendo los múltiplos de 3 por la palabra
“fizz”, los múltiplos de 5 por “buzz” y los múltiplos de ambos, es decir, los múltiplos de 3 y 5 (o de 15),
por la palabra “fizzbuzz”.

"""
i = 1

# Primer intento
while i <= 100:
    if i % 3 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        print('Fizz')
    elif i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        print('Buzz')
    else:
        print(i)
    i += 1

# Mejorando el primer intento
while i <= 100:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
    i += 1

# Con for
for n in range(1, 101):
    if n % 15 == 0:
        print('FizzBuzz')
    if n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)
