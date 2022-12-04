# alto = 5
# base = 20
#
# for i in range(base):
#     print('*' * i)

# nombres = []
# while True:
#     a = str(input('Ingrese las partes: '))
#     if a != "":
#         nombres.append(a)
#     else:
#         break
#
# print(nombres)
# nombres.sort()
# print(nombres)

# cadena = 'Developer'
# cadena = cadena.upper()
# # cadena = list(cadena)
#
# for i in range(1, (len(cadena) + 1)):
#     print(cadena[0:i])

# print(cadena[0:2])
n = 15

for i in range(1, n + 1):
    print('*' * i)

for i in range(1, n + 1):
    espacio = n - i
    print(' '*espacio, '*' * i)

for i in range(1, n + 1):
    espacio = n - i
    print(' '*espacio, '* ' * i)

for i in range(1, n + 1):
    espacio = n - i
    print(' '*espacio, '*' * i, '*' * i)

