"""

/*
 * Reto #40
 * TRIÁNGULO DE PASCAL
 * Fecha publicación enunciado: 03/10/22
 * Fecha publicación resolución: 10/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole
 * únicamente el tamaño del lado.
 * - Aquí puedes ver rápidamente cómo se calcula el triángulo:
 *   https://commons.wikimedia.org/wiki/File:PascalTriangleAnimated2.gif
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""
# j = 10
# for i in range(1, j):
#     # print((j - i) * '-', (i * f'{i} '), (j - i) * '-')
#     espacio = (j - i) * ' '
#     print(espacio, (i * f'{i} '), espacio)

j = int(input('Ingrese el tamaño del triangulo: '))
# listas = []
# for i in range(1, j):
#     resultado = [i for _ in range(1, i + 1)]
#     listas.append(resultado)


# listas = [[i for _ in range(1, i + 1)] for i in range(1, j)]
# print(listas)

# for lista in listas:
#     print(lista)


def find_next_list(lista_ret):
    retorno = []

    rango = len(lista_ret)
    menor = min(range(rango))
    mayor = max(range(rango))

    for i in range(rango):

        if menor == i:
            retorno.append(lista_ret[i])

        if i < rango - 1:
            retorno.append(lista_ret[i] + lista_ret[i + 1])

        if mayor == i:
            retorno.append(lista_ret[i])

    return retorno


# inicial = [1]
# listas = []
#
# for _ in range(1, j + 1):
#     listas.append(inicial)
#     inicial = find_next_list(inicial)

inicial = [1]
listas = [inicial] + [inicial := find_next_list(inicial) for _ in range(1, j)]

for lista in listas:
    g = j - len(lista)
    texto = ', '.join(map(str, lista))
    print(g * ' ', texto)


