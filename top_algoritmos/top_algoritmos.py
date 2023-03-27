"""

/*
 * Reto #39
 * TOP ALGORITMOS: QUICK SORT
 * Fecha publicación enunciado: 27/09/22
 * Fecha publicación resolución: 03/10/22
 * Dificultad: MEDIA
 *
 * Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort",
 * creado por C.A.R. Hoare.
 * - Entender el funcionamiento de los algoritmos más utilizados de la historia nos ayuda a
 * mejorar nuestro conocimiento sobre ingeniería de software. Dedícale tiempo a entenderlo,
 * no únicamente a copiar su implementación.
 * - Esta es una nueva serie de retos llamada "TOP ALGORITMOS", donde trabajaremos y entenderemos
 * los más famosos de la historia.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""
import random

elementos = [6, 3, 1, 2, 4, 8, 5, 9, 6, 4, 2, 6, 0, 8, 4]


# Nota (Lenin Elio - 26/03/2023 16:32)
# Tomando el primer elemento de la lista
def quicksort_fe(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]

        menores = [x for x in lista[1:] if x < pivote]
        mayores = [x for x in lista[1:] if x >= pivote]
        return quicksort_fe(menores) + [pivote] + quicksort_fe(mayores)


# Nota (Lenin Elio - 26/03/2023 16:40)
# Usando la regla, mediana de tres
def quicksort_mt(lista):
    if len(lista) <= 1:
        return lista
    else:
        primero = lista[0]
        ultimo = lista[-1]
        medio = lista[len(lista) // 2]
        pivote = sorted([primero, ultimo, medio])[1]

        menores = [x for x in lista if x < pivote]
        mayores = [x for x in lista if x > pivote]
        iguales = [x for x in lista if x == pivote]
        return quicksort_mt(menores) + iguales + quicksort_mt(mayores)


# Nota (Lenin Elio - 26/03/2023 16:44)
# Eligiendo un elemento aleatorio
def quicksort_re(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = random.choice(lista)

        menores = [x for x in lista if x < pivote]
        mayores = [x for x in lista if x > pivote]
        iguales = [x for x in lista if x == pivote]
        return quicksort_re(menores) + iguales + quicksort_re(mayores)


print(quicksort_fe(elementos))
print(quicksort_mt(elementos))
print(quicksort_re(elementos))
