"""

/*
 * Reto #10
 * EXPRESIONES EQUILIBRADAS
 * Fecha publicación enunciado: 07/03/22
 * Fecha publicación resolución: 14/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
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
entrada = '{ a * ( c + d ) ] - 5 }'

pares = {'(': ')', '{': '}', '[': ']'}
ar = pares.keys()
ax = pares.values()
lista = list(ar) + list(ax)

valor_encontrado = []
valor_esperado = []
for j in entrada:
    for a, b in pares.items():
        if j == a:
            valor_encontrado.append(j)
            valor_esperado.append(b)

union = valor_encontrado + valor_esperado[::-1]
union = ''.join(union)
reform_entrada = ''
for s in entrada:
    for t in lista:
        if s == t:
            reform_entrada += s

if reform_entrada == union:
    print(f'{entrada} es una expresión balanceada')
else:
    print(f'{entrada} no es una expresión balanceada')


