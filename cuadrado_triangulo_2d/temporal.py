# alto = 5
# base = 20
#
# for i in range(base):
#     print('*' * i)

nombres = []
while True:
    a = str(input('Ingrese las partes: '))
    if a != "":
        nombres.append(a)
    else:
        break

print(nombres)
nombres.sort()
print(nombres)
