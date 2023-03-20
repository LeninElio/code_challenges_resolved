"""

/*
 * Reto #36
 * LOS ANILLOS DE PODER
 * Fecha publicación enunciado: 06/09/22
 * Fecha publicación resolución: 14/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales a Sauron
 * contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
 * Cada raza tiene asociado un "valor" entre 1 y 5:
 * - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
 * - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
 * Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
 * - El resultado puede ser que gane el bien, el mal, o exista un empate. Dependiendo de la
 * suma del valor del ejército y el número de integrantes.
 * - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
 * - Tienes total libertad para modelar los datos del ejercicio.
 * Ej: 1 Peloso pierde contra 1 Orco, 2 Pelosos empatan contra 1 Orco, 3 Pelosos ganan a 1 Orco.
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""
razas = {
    'bondadosas': {'Pelosos': 1, 'Sureños buenos': 2, 'Enanos': 3, 'Númenóreanos': 4, 'Elfos': 5},
    'malvadas': {'Sureños malos': 2, 'Orcos': 2, 'Goblins': 2, 'Huargos': 3, 'Trolls': 5}
}


# Nota (Lenin Elio - 19/03/2023 21:44)
# Batalla entre dos razas
def batalla_razas(atacante, integrantes_a, oponente, integrantes_o):
    r_bondadosa = razas['bondadosas']
    r_malvada = razas['malvadas']

    mensaje = ''
    if integrantes_o <= 0 or integrantes_a <= 0:
        return 'Debe haber al menos un integrante en el ejercito.'

    if atacante in r_bondadosa and oponente in r_malvada:
        buenos = r_bondadosa[atacante] * integrantes_a
        malos = r_malvada[oponente] * integrantes_o
        if buenos == malos:
            mensaje = 'Ha sido un empate.'
        elif buenos > malos:
            mensaje = 'Gana el bien.'
        else:
            mensaje = 'Gana el mal.'
    else:
        mensaje = 'Atacante u oponente no encontrado.'

    return mensaje


# Nota (Lenin Elio - 19/03/2023 21:43)
# Batalla entre ejércitos
def poder(**kwargs):
    poder_total = 0
    for c, v in kwargs.items():
        for cl, vl in v.items():
            poder_total += razas[c][cl] * vl
    return poder_total


def validar(**kwargs):
    valor = [*kwargs][0]
    clave_k = set(kwargs[valor].keys())
    clave_r = set(razas[valor].keys())

    result = clave_k.difference(clave_r)

    values = kwargs[[*kwargs][0]].values()
    values = sorted(values)[0]

    if values <= 0:
        return True
    elif len(result) > 0:
        return True
    else:
        return False


def batalla_ejercito(**kwargs):
    r_bondadosa = kwargs['bondadosas']
    r_malvada = kwargs['malvadas']

    if validar(bondadosas=r_bondadosa) or validar(malvadas=r_malvada):
        return 'Revise los valores ingresados.'

    p_bondadosa = poder(bondadosas=r_bondadosa)
    p_malvada = poder(malvadas=r_malvada)

    mensaje = ''
    if p_bondadosa == p_malvada:
        mensaje = 'Ha sido un empate.'
    elif p_bondadosa > p_malvada:
        mensaje = 'Gana el bien.'
    else:
        mensaje = 'Gana el mal.'

    return mensaje


bondadosas = {'Pelosos': 20, 'Sureños buenos': 20, 'Enanos': 30, 'Númenóreanos': 40, 'Elfos': 30}
malvadas = {'Sureños malos': 20, 'Orcos': 20, 'Goblins': 20, 'Huargos': 30, 'Trolls': 50}

resultado_ejercito = batalla_ejercito(bondadosas=bondadosas, malvadas=malvadas)
print(resultado_ejercito)

