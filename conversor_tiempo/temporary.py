# def ingreso():
#     hora = int(input('Ingrese la cantidad de horas: '))
#     while True:
#         if hora > 60:
#             hora = int(input('La cantidad de horas no debe superar 60: '))
#         elif hora < 0:
#             hora = int(input('La cantidad de horas no debe ser menor a 0: '))
#         else:
#             return hora
#
#
# print(ingreso())

def valida(numero, mini, maxi):
    while True:
        if mini <= numero <= maxi:
            return numero
        else:
            numero = int(input(f'Este valor debe estar entre {mini} y {maxi}: '))


hora = int(input('Ingrese la cantidad de horas: '))
hora = valida(hora, 1, 59)

print(hora)
