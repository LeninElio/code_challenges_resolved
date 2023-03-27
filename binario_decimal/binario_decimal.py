"""

/*
 * Reto #38
 * BINARIO A DECIMAL
 * Fecha publicación enunciado: 19/09/22
 * Fecha publicación resolución: 27/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar
 * funciones propias del lenguaje que lo hagan directamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""


def decimal_binario(numero):
    i = numero
    binario = []

    while i >= 1:
        num = i % 2
        binario.append(num)
        i //= 2

    resultado = ''.join([str(x) for x in binario[::-1]])
    return f'{numero} en binario es: {resultado}'


def binario_decimal(binario):
    decimal, i = 0, binario
    binario = list(binario)
    for indice, valor in enumerate(binario[::-1]):
        decimal += int(valor) * (2 ** indice)

    return f'{i} en decimal es: {decimal}'


# number = int(input('Ingrese el numero a convertir en binario: '))
# print(decimal_binario(number))
binario_in = str(input('Ingrese el binario a convertir en decimal: '))
bina = binario_decimal(binario_in)
print(bina)
