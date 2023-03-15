"""

 * Reto #32
 * EL SEGUNDO
 * Fecha publicación enunciado: 08/08/22
 * Fecha publicación resolución: 15/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Dado un listado de números, encuentra el SEGUNDO más grande.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas,
     dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en https://retosdeprogramacion.com/semanales2022.
 *
 */

"""

lista = [1, 4, 5, 6, 7, 8, 2]

n = len(lista)

for i in range(n):
    for j in range(0, n - i - 1):
        if lista[j] < lista[j + 1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(lista[1])



