"""

/*
 * Reto #31
 * AÑOS BISIESTOS
 * Fecha publicación enunciado: 01/08/22
 * Fecha publicación resolución: 08/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que imprima los 30 próximos años bisiestos siguientes a uno dado.
 * - Utiliza el menor número de líneas para resolver el ejercicio.
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


# Nota (Lenin Elio - 13/03/2023 15:59), esta function busca un año bisiesto
def a_bisiesto(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


lista = []

# Nota (Lenin Elio - 13/03/2023 15:59), while para la búsqueda de los 30 primeros años bisiesto
a_inicio = int(input('Ingrese un año de inicio: '))
while len(lista) < 30:
    if a_bisiesto(a_inicio):
        lista.append(a_inicio)
    a_inicio += 1


# Nota (Lenin Elio - 13/03/2023 16:09), resultado mas reducido en el archivo temporal
print(lista)
