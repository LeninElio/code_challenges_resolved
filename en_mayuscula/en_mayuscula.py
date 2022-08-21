"""

/*
 * Reto #16
 * EN MAYÚSCULA
 * Fecha publicación enunciado: 18/04/22
 * Fecha publicación resolución: 25/04/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
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
cadena = str(input('Ingrese un párrafo: '))
cadena = cadena.split(' ')

nueva_cadena = []
for i in cadena:
    x = i.replace(i[0], i[0].upper())
    d = i[1:].lower()
    n = x[0] + d
    nueva_cadena.append(n)

nueva_cadena = ' '.join(nueva_cadena)
cadena = ' '.join(cadena)
print(cadena)
print(nueva_cadena)
