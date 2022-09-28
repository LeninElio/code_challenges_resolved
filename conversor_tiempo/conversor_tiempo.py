"""

/*
 * Reto #19
 * CONVERSOR TIEMPO
 * Fecha publicación enunciado: 09/05/22
 * Fecha publicación resolución: 16/05/22
 * Dificultad: FACIL
 *
 * Enunciado: Crea una función que reciba días, horas, minutos y segundos (como enteros)
    y retorne su resultado en milisegundos.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas,
    dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */

"""


def conversor(dias, horas, minutos, segundos):
    # def conversor(dias):
    dia_m = dias * 24 * 60 * 60 * 1000
    hora_m = horas * 60 * 60 * 1000
    minuto_m = minutos * 60 * 1000
    segundo_m = segundos * 1000
    return dia_m, hora_m, minuto_m, segundo_m


def valida(numero, mini, maxi):
    while True:
        if mini <= numero <= maxi:
            return numero
        else:
            numero = int(input(f'Este valor debe estar entre {mini} y {maxi}: '))


dia = int(input('Ingrese la cantidad de dias: '))

hora = int(input('Ingrese la cantidad de horas: '))
hora = valida(hora, 1, 23)

minuto = int(input('Ingrese la cantidad de minutos: '))
minuto = valida(minuto, 1, 59)

segundo = int(input('Ingrese la cantidad de segundos: '))
segundo = valida(segundo, 1, 59)

# milisegundo = conversor(dia, hora, minuto, segundo)
m_dia, m_hora, m_minuto, m_segundo = conversor(dia, hora, minuto, segundo)

# print(f'{dia} dias, {hora} horas, {minuto} minutos, {segundo} segundos')
print('*' * 35)
print(f'{dia} dias en milisegundos es: {m_dia}')
print(f'{hora} horas en milisegundos es: {m_hora}')
print(f'{minuto} minutos en milisegundos es: {m_minuto}')
print(f'{segundo} segundos en milisegundos es: {m_segundo}')
print('*' * 35)
print(f'El total es: {m_dia + m_hora + m_minuto + m_segundo}')
# print(f'Expresados en milisegundos es: {milisegundo}')
