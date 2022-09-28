"""

/*
 * Reto #18
 * TRES EN RAYA
 * Fecha publicación enunciado: 02/05/22
 * Fecha publicación resolución: 09/05/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */

"""


lista = [5, 1, 2, 3, 4, 6, 'x']
# lista.sort()

for i in lista:
    if i == lista[-1]:
        print(i, end='')
    else:
        print(i, end='-')

print()

var = [i == 'x' for i in lista]
print(var)

# for i in range(len(lista)):
#     if lista[i] == lista[-1]:
#         print(lista[i], end='')
#     else:
#         print(lista[i], end='-')
#
# print()

for j in lista:
    print(j, sep='+')
#
# for i in lista:
#     for j in i:
#         print(i, j)

# var = [i for m in lista for i in m]
# print(var)


# for i in range(len(lista)):
#     print('[', end='')
#     for j in range(len(lista[i])):
#         print('{:>3s}'.format(str(lista[i][j])), end='')
#     print(']')
#
