"""
 * Reto #6
 * INVIRTIENDO CADENAS
 * Fecha publicación enunciado: 07/02/22
 * Fecha publicación resolución: 14/02/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que
    lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar
    ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 """

cadena = 'Esta cadena sera invertida'
# print(type(cadena))

# print(len(cadena))
# print(cadena[0] + cadena[7])
invertida = ''
i = len(cadena) - 1
while i > -1:
    invertida += cadena[i]
    i -= 1
print(invertida)


# Intento mejorado con For
salida = ''
for i in range(0, len(cadena)):
    salida += cadena[-i]
    print('resultado: ', salida)
print(salida)

