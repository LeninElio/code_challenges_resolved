"""

/*
 * Reto #33
 * CICLO SEXAGENARIO CHINO
 * Fecha publicación enunciado: 15/08/22
 * Fecha publicación resolución: 22/08/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un función, que dado un año, indique el elemento y animal correspondiente
 * en el ciclo sexagenario del zodíaco chino.
 * - Información: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
 * - El ciclo sexagenario se corresponde con la combinación de los elementos madera,
 *   fuego, tierra, metal, agua y los animales rata, buey, tigre, conejo, dragón, serpiente,
 *   caballo, oveja, mono, gallo, perro, cerdo (en este orden).
 * - Cada elemento se repite dos años seguidos.
 * - El último ciclo sexagenario comenzó en 1984 (Madera Rata).
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas,
     dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en https://retosdeprogramacion.com/semanales2022.
 *
 */

"""

elementos = ['madera', 'fuego', 'tierra', 'metal', 'agua']
animales = ['rata', 'buey', 'tigre', 'conejo', 'dragón', 'serpiente',
            'caballo', 'oveja', 'mono', 'gallo', 'perro', 'cerdo']


def ciclo_sexagenario_chino(valor):
    if valor < 1984:
        return 'El último ciclo sexagenario comenzó en 1984 (Madera Rata). Introduce un año a partir de entonces.'

    indice_elemento = (valor - 1984) // 2 % len(elementos)
    indice_animal = (valor - 1984) % len(animales)

    return f'{elementos[indice_elemento]} {animales[indice_animal]}'


lista = [2022, 2023, 2024, 2025, 2026, 2027]
for i in lista:
    print(ciclo_sexagenario_chino(i))
