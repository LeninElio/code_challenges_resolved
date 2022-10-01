"""

/*
 * Reto #22
 * CONJUNTOS
 * Fecha publicación enunciado: 01/06/22
 * Fecha publicación resolución: 07/06/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
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


def comparar(list1, list2, valor):
    comunes = []
    no_comunes = []
    for i in list1:
        if i in list2:
            comunes.append(i)
        else:
            no_comunes.append(i)

    for i in list2:
        if i in list1:
            comunes.append(i)
        else:
            no_comunes.append(i)

    comunes, no_comunes = set(comunes), set(no_comunes)
    comunes, no_comunes = list(comunes), list(no_comunes)

    if valor:
        return comunes
    else:
        return no_comunes


list_one = [1, 2, 3, 4, 5, 'a', 'b', 'c']
list_two = [5, 'b', 'c', 7, 8, 'e']
value = False

boole = ''
if value:
    boole = 'Verdadero, retorna lo valores comunes'
else:
    boole = 'Falso, retorna lo valores no comunes'

resultado = comparar(list_one, list_two, value)
print('Cuando el valor es {}: {}'.format(boole, resultado))
