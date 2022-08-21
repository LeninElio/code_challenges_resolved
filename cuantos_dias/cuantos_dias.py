"""

/*
 * Reto #15
 * ¿CUÁNTOS DÍAS?
 * Fecha publicación enunciado: 11/04/22
 * Fecha publicación resolución: 18/04/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar
     ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */

"""
from functools import reduce

# fec_01 = "18/02/2024"
# fec_02 = "20/08/2023"
#
# fec_01 = fec_01.split('/')
# fec_02 = fec_02.split('/')
#
#
# def mayor():
#     if int(fec_01[2]) > int(fec_02[2]):
#         return fec_01, fec_02
#     elif int(fec_02[2]) > int(fec_01[2]):
#         return fec_02, fec_01
#     else:
#         if int(fec_01[1]) > int(fec_02[1]):
#             return fec_01, fec_02
#         elif int(fec_02[1]) > int(fec_01[1]):
#             return fec_02, fec_01
#         else:
#             if int(fec_01[0]) > int(fec_02[0]):
#                 return fec_01, fec_02
#             elif int(fec_02[0]) > int(fec_01[0]):
#                 return fec_02, fec_01
#             else:
#                 return 'Misma', 'fecha'
#
#
# may_fecha, men_fecha = mayor()
#
# may_an = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
#           '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
#
# men_an = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
#           '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}
#

# def bisiesto(anio):
#     if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
#         return True
#     else:
#         return False
#
#
# def febrero():
#     may_feb = bisiesto(int(may_fecha[2]))
#     men_feb = bisiesto(int(men_fecha[2]))
#
#     if may_feb:
#         may_an['02'] = str(29)
#
#     if men_feb == 29:
#         men_an['02'] = str(28)
#
#
# febrero()
#
# # val = reduce(lambda x, y: int(x) + int(y), may_an.values())
#
#
# # for n in range(1, val + 1):
#
# #
# # suma = 0
# # for cl, vl in may_an.items():
# #     suma += int(vl)
# #     for n in range(1, val + 1):
# #         if n == suma:
# #             print(cl, n)
#
# # def retorna_num(da, mes, an):
# #     da = int(da)
# #     suma = 0
# #     for cl, vl in an.items():
# #         suma += int(vl)
# #         for n in range(1, val + 1):
# #             if n == (suma + da) and cl == mes:
# #                 return n
#
#
# # print(retorna_num('31', '12', may_an))
#
#
# def retorna_num(da, mes, an):
#     da = int(da)
#     suma = 0
#     for cl, vl in an.items():
#         suma += int(vl)
#         if cl == mes:
#             retorno = suma - (int(vl) - da)
#             return retorno
#
#
# # print(retorna_num(may_fecha[0], may_fecha[1], may_an))
# residuo = []
# dif_an = int(may_fecha[2])
# while dif_an >= int(men_fecha[2]):
#     residuo.append(dif_an)
#     dif_an -= 1
#
# # print(residuo)
# # print(len(residuo))
# # val = reduce(lambda x, y: int(x) + int(y), an.values())
# # if len(residuo) == 1:
# mayor_aio = retorna_num(may_fecha[0], may_fecha[1], may_an)
# menor_aio = retorna_num(men_fecha[0], men_fecha[1], men_an)
# resta_dias = mayor_aio - menor_aio
# print(resta_dias)
# print(menor_aio)
# print(mayor_aio)

# else:
#     for i in residuo:
#         if bisiesto(i):
#             bis = 366
#             print(bis)
#             if i == residuo[-1]:
#                 das =
#                 print('final', i)
#             else:
#                 print('hay aun', i)
#         else:
#             bis = 365
#             print(bis)
#             if i == residuo[-1]:
#                 print('final', i)
#             else:
#                 print('hay aun', i)

# a = int(may_fecha[2]) - int(men_fecha[2])
# m = int(may_fecha[1]) - int(men_fecha[1])
# d = int(may_fecha[0]) - int(men_fecha[0])
#
# print(f'{d} dias {m} meses {a} años')
#
# dias = int(men_an[men_fecha[1]]) - int(men_fecha[0])
# dia = int(may_fecha[0]) - 0

# print(dias + dia)
