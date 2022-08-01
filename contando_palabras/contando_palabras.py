"""
 * Reto #7
 * CONTANDO PALABRAS
 * Fecha publicación enunciado: 14/02/22
 * Fecha publicación resolución: 21/02/22
 * Dificultad: MEDIA
 *
 * Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 """

palabras = 'Hola, mi nombre es lenin elio, Mi nombre completo es Lenin Elio Moreno Vega (leninelio)'

palabra = ''

# for i in range(0, len(palabras)):
#     if palabras[i] == "":
#         # print('espacio')
#         palabra += palabras[i]
#         # continue
#     elif palabras[i] == ",":
#         # print('coma')
#         continue
#     else:
#         # palabra += palabras[i]
#         continue
# print(palabra)


for i in range(0, len(palabras)):
    if palabras[i] == ",":
        continue
    else:
        palabra += palabras[i]

data = palabra.split(' ')
zata = data

for i in data:
    print(zata)
    zata.remove(i)
    print(zata)
    for j in zata:
        if i == j:
            print(i)
        else:
            print('No se')

print(data)
print(zata)