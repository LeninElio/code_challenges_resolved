"""

/*
 * Reto #26
 * CUADRADO Y TRIÁNGULO 2D
 * Fecha publicación enunciado: 27/06/22
 * Fecha publicación resolución: 07/07/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
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


def cuadrado(alto, ancho):
    for _ in range(alto):
        print('*   ' * ancho)


def triangulo(alto):
    for j in range(1, alto + 1):
        espacio = alto - j
        print(' ' * espacio, '* ' * j)


while True:
    print("""
    1.- Cuadrado
    2.- Triangulo
    3.- Salir
    """)
    i = int(input('Ingrese un valor: '))

    if i == 1:
        print('-' * 45)
        print('Has elegido Cuadrado')
        altura = int(input('Ingresa la altura: '))
        anchura = int(input('Ingresa la anchura: '))
        cuadrado(altura, anchura)
        print('-' * 45)
        break
    elif i == 2:
        print('-' * 45)
        print('Has elegido Triangulo')
        altura = int(input('Ingresa el alto del Triangulo: '))
        triangulo(altura)
        print('-' * 45)
        break
    elif i == 3:
        break
