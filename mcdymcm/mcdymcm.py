"""

/*
 * Reto #23
 * MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO
 * Fecha publicación enunciado: 07/06/22
 * Fecha publicación resolución: 13/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra que calcule el mínimo
    común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
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


def mcd_values(num):
    primos = [2, 3, 5, 7, 11, 13]
    lista = []
    for i in primos:
        while num % i == 0:
            if num % i == 0:
                # valor[num] = i
                lista.append(i)
                num = num / i
            else:
                continue

    # return valor
    return lista


def mcd(num1, num2):
    lista_1 = mcd_values(num1)
    lista_2 = mcd_values(num2)

    list1 = [i for i in lista_1 if i in lista_2]
    list2 = [i for i in lista_2 if i in lista_1]

    if len(list1) > len(list2):
        f_lista = [i for i in list2 if i in list1]
    elif len(list2) > len(list1):
        f_lista = [i for i in list1 if i in list2]
    else:
        f_lista = [i for i in list1 if i in list2]

    multi = 1
    for i in f_lista:
        multi *= i

    return f'El máximo común divisor de {num1} y {num2} es {multi}'


def mcm_values(num):
    primos = [2, 3, 5, 7]
    lista = []
    for i in primos:
        while num % i == 0:
            if num % i == 0:
                lista.append(i)
                num = num / i
            else:
                continue
    return lista


def mcm(num1, num2):
    lista_1 = mcd_values(num1)
    lista_2 = mcd_values(num2)

    lista2 = [i for i in lista_2 if i not in lista_1]
    lista3 = lista_1 + lista2

    multi = 1
    for i in lista3:
        multi *= i

    return f'El mínimo común múltiplo de {num1} y {num2} es {multi}'


print(mcd(380, 420))
print(mcm(75, 25))

