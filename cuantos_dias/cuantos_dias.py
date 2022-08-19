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

fec_01 = "10/12/2021"
fec_02 = "12/09/2024"

fec_01 = fec_01.split('/')
fec_02 = fec_02.split('/')

mes1 = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
        '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}

mes2 = {'01': '31', '02': '28', '03': '31', '04': '30', '05': '31', '06': '30',
        '07': '31', '08': '31', '09': '30', '10': '31', '11': '30', '12': '31'}


def bisiesto(anio):
    if anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0):
        return 29
    else:
        return 28


def febrero():
    feb1 = bisiesto(int(fec_01[2]))
    feb2 = bisiesto(int(fec_02[2]))

    if feb1 == 29:
        mes1['02'] = str(feb1)

    if feb2 == 29:
        mes2['02'] = str(feb2)


febrero()
print(mes1)
print(mes2)

for i in range(1, int(fec_02[1]) + 1):
    print(i)
