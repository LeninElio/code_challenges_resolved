"""

/*
 * Reto #17
 * LA CARRERA DE OBSTÁCULOS
 * Fecha publicación enunciado: 25/04/22
 * Fecha publicación resolución: 02/05/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 * - Un array que solo puede contener String con las palabras "run" o "jump"
 * - Un String que represente la pista y solo puede contener "_" (suelo) o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 * - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla) será correcto y no
 * variará el símbolo de esa parte de la pista.
 * - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 * - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
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
from random import choice

diccionario = {'run': '_', 'jump': '|'}

k = list(diccionario.keys())
v = list(diccionario.values())

intentos = 5
i = 0

entrada = ''
while i < intentos:
    aleatorio = choice(k)
    select = str(input(f'Ingrese el valor para {aleatorio}: '))
    if select == '_' and aleatorio == 'run':
        entrada += select
    elif select == '|' and aleatorio == 'jump':
        entrada += select
    elif aleatorio == 'run' and select != '_':
        entrada += 'X'
    elif aleatorio == 'jump' and select != '|':
        entrada += '/'
    i += 1


count = 0
for i in range(len(entrada)):
    if entrada[i] in v:
        pass
    else:
        count += 1


entrada = ''.join(entrada)
print(f'Te haz equivocado {count} veces')
