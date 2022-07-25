# Primer intento
a = str(input('Ingrese la primera palabra: '))
b = str(input('Ingrese la segunda palabra: '))

c1 = set(a)
c2 = set(b)

if c1 == c2:
    print('Es un anagrama')
else:
    print('No es un anagrama')


# Primer intento mejorado
n = set(input('Ingrese la primera palabra: '))
m = set(input('Ingrese la segunda palabra: '))

if n == m:
    print('Es un anagrama')
else:
    print('No es un anagrama')
