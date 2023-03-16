"""

/*
 * Reto #35
 * BATALLA POKÉMON
 * Fecha publicación enunciado: 29/08/22
 * Fecha publicación resolución: 06/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
 * - La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
 * - Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
 * - Sólo hay 4 tipos de Pokémon: Agua, Fuego, Planta y Eléctrico (buscar su efectividad)
 * - El programa recibe los siguientes parámetros:
 *  - Tipo del Pokémon atacante.
 *  - Tipo del Pokémon defensor.
 *  - Ataque: Entre 1 y 100.
 *  - Defensa: Entre 1 y 100.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""

tipo = {
    'Agua': {
        'Super efectivo': ['Fuego'],
        'Neutro': ['Eléctrico', 'Agua'],
        'No efectivo': ['Planta']
    },
    'Fuego': {
        'Super efectivo': ['Planta'],
        'Neutro': ['Eléctrico', 'Fuego'],
        'No efectivo': ['Agua']
    },
    'Planta': {
        'Super efectivo': ['Agua'],
        'Neutro': ['Eléctrico', 'Planta'],
        'No efectivo': ['Fuego']
    },
    'Eléctrico': {
        'Super efectivo': ['Agua'],
        'Neutro': ['Fuego', 'Eléctrico'],
        'No efectivo': ['Planta']
    },
}

efectividad = {
    'Super efectivo': 2,
    'Neutro': 1,
    'No efectivo': 0.5
}


def batalla_pokemon(atacante, defensor, ataque, defensa):
    # Nota (Lenin Elio - 15/03/2023 21:05)
    # Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
    # daño = 50 * (ataque / defensa) * efectividad
    if not (1 <= ataque <= 100) or not (1 <= defensa <= 100):
        return 'El ataque o defensa deben ser menores a 100'

    if atacante not in tipo or defensor not in tipo:
        return 'Atacante o defensor no encontrado'

    for indice, valor in tipo[atacante].items():
        if defensor in valor:
            danio = 50 * (ataque / defensa) * efectividad[indice]
            return danio


resultado = batalla_pokemon('Agua', 'Agua', 60, 80)
print(resultado)
