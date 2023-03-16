"""

/*
 * Reto #34
 * LOS NÚMEROS PERDIDOS
 * Fecha publicación enunciado: 22/08/22
 * Fecha publicación resolución: 29/08/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Dado un array de enteros ordenado y sin repetidos, crea una función que calcule
 * y retorne todos los que faltan entre el mayor y el menor.
 * - Lanza un error si el array de entrada no es correcto.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""


def valores_faltantes(array):
    if not isinstance(array, list) or len(array) == 0 or len(array) != len(set(array)) or array != sorted(array):
        return "El array de entrada no es válido o no está ordenado"

    min_val = min(array)
    max_val = max(array)
    full_list = list(range(min_val, max_val + 1))
    missing_vals = list(set(full_list) - set(array))

    return missing_vals


arreglo = [1, 2, 5, 7, 8, 10, 34]
print(valores_faltantes(arreglo))
