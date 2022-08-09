"""
/*
 * Reto #9
 * CÓDIGO MORSE
 * Fecha publicación enunciado: 02/03/22
 * Fecha publicación resolución: 07/03/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
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

# morse = {'B': '1000', 'A': '01'}
# arma = []

# for a, b in morse.items():
#     # print(b)
#     if len(b) == 0:
#         for t in b:
#             if t == '0':
#                 arma.append('-')
#             elif t == '1':
#                 arma.append('.')
#     else:
#         arma.append(' ')
#     # arma = ''.join(arma)
#
# print(arma)
#
#
# def convertir(an, bn):
#     lista = bn
#
#
# conde = '10101'

# for t in conde:
#     if t == '0':
#         arma.append('-')
#     elif t == '1':
#         arma.append('.')
#
# arma = ''.join(arma)
# print(arma)

palabra = str(input('Ingrese una palabra para convertir en morse: '))

palabra = palabra.upper()

morse = {'A': '.-', 'N': '-.', 'B': '-...', 'O': '---', 'C': '-.-.', 'P': '.--.', 'D': '-..', 'Q': '--.-', 'E': '.',
         'R': '.-.', 'F': '..-.', 'S': '...', 'G': '--.', 'T': '-', 'H': '....', 'U': '..-', 'I': '..', 'V': '...-',
         'J': '.---', 'W': '.--', 'K': '-.-', 'X': '-..-', 'L': '.-..', 'Y': '-.--', 'M': '--', 'Z': '--..',
         ' ': '/'}

reco = []

for i in palabra:
    for j in morse:
        if i == j:
            reco.append(morse[j])
            reco.append(' ')
reco = ''.join(reco)
print(reco)
