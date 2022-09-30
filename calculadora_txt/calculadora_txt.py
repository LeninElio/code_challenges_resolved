"""

/*
 * Reto #21
 * CALCULADORA .TXT
 * Fecha publicación enunciado: 23/05/22
 * Fecha publicación resolución: 01/06/22
 * Dificultad: MEDIA
 *
 * Enunciado: Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*" y división "/".
 * - El resultado se muestra al finalizar la lectura de la última línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han podido resolver las operaciones.
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

with open('Challenge21.txt', mode='r', encoding='UTF-8') as file:
    archivo = file.readlines()
    datos = []
    for i in archivo:
        datos.append(i.strip())

    str_conversion = []
    operadores = []
    for i in datos:
        try:
            str_conversion.append(float(i))
        except ValueError:
            str_conversion.append(i)
            operadores.append(i)

    if type(str_conversion[0]) == int or type(str_conversion[0]) == float:
        resultado = 0
        operador = '+'
        for i in range(len(str_conversion)):
            if i == 0:
                resultado = str_conversion[i]
                continue
            if str_conversion[i] in operadores:
                operador = str_conversion[i]
                continue
            else:
                if operador == '+':
                    resultado += str_conversion[i]
                elif operador == '-':
                    resultado -= str_conversion[i]
                elif operador == '*':
                    resultado *= str_conversion[i]
                elif operador == '/':
                    resultado /= str_conversion[i]

        print(f'Datos leídos: {datos}')
        print(f'Resultado: {resultado}')
    else:
        print('Archivo en formato in correcto.')
    file.close()
