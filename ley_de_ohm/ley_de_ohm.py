"""

/*
 * Reto #41
 * LA LEY DE OHM
 * Fecha publicación enunciado: 10/10/22
 * Fecha publicación resolución: 17/10/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
 * - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
 * - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".

    V es el potencial eléctrico en voltios.
    I es la corriente en amperios.
    R es la resistencia en ohms.

 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""


def ley_de_ohm(v=None, i=None, r=None):
    mensaje = ''
    try:
        if v is None:
            mensaje = f'V = {round(i * r, 2)} voltios'
        elif i is None:
            mensaje = f'I = {round(v / r, 2)} amperios'
        elif r is None:
            mensaje = f'R = {round(v / i, 2)} ohmios'
    except:
        mensaje = 'Invalid values'

    return mensaje


print(ley_de_ohm(v=3, i=6))
