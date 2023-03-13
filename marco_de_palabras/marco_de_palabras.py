"""

/*
 * Reto #30
 * MARCO DE PALABRAS
 * Fecha publicación enunciado: 26/07/22
 * Fecha publicación resolución: 01/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un texto y muestre cada palabra en una línea, formando
 * un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
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


# Nota (Lenin Elio - 13/03/2023 12:35), definimos la function
def marco_de_palabras(texto):
    palabras = texto.split(' ')
    mayor = 0

    # Nota (Lenin Elio - 13/03/2023 12:33), Este for devuelve el texto con más letras
    for i in palabras:
        if len(i) > mayor:
            mayor = len(i)
        else:
            mayor = mayor

    print('*' * (mayor + 4))

    # Nota (Lenin Elio - 13/03/2023 12:34), for donde se imprime las palabras, si hay espacios en blanco en exceso
    # no se imprimen
    for palabra in palabras:
        if palabra.strip() != '':
            print('*', palabra + ' ' * (mayor - len(palabra)), '*')
    print('*' * (mayor + 4))


# Nota (Lenin Elio - 13/03/2023 12:35), probamos la function
marco_de_palabras('  hola mundos del       universo he venido de la galaxia andromeda')

