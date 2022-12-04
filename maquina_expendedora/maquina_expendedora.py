"""
/*
 * Reto #28
 * MÁQUINA EXPENDEDORA
 * Fecha publicación enunciado: 11/07/22
 * Fecha publicación resolución: 18/07/22
 * Dificultad: MEDIA
 *
 * Enunciado: Simula el funcionamiento de una máquina expendedora creando una operación
 * que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor
 *   número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje
 * y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o
     prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */
"""

productos = {
    1: ["Agua", 50],
    2: ["Coca-Cola", 100],
    4: ["Cerveza", 155],
    5: ["Pizza", 200],
    10: ["Donut", 75]
}

# for i, j in productos.items():
#     print(f'Presione: {i} -> {j[0]}, S/.{j[1]}')


def moneda(valor):
    monedas = {
        'cinco': 5,
        'diez': 10,
        'cincuenta': 50,
        'cien': 100,
        'doscientos': 200
    }
    estado = 0
    for x, y in monedas.items():
        if x == valor:
            estado = y
            break
        else:
            estado = 0

    return estado


