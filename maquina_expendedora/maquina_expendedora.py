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


def maquina_expendedora(monedas, seleccion):
    productos = {
        1: ["Agua", 50],
        2: ["Coca-Cola", 100],
        3: ["Cerveza", 155],
        4: ["Pizza", 200],
        5: ["Donut", 75]
    }

    monedas_soportadas = [5, 10, 50, 100, 200]
    total = sum(monedas)

    # Verificar si las monedas son soportadas
    for moneda in monedas:
        if moneda not in monedas_soportadas:
            return "Moneda no soportada", monedas

    # Verificar si el producto existe
    if seleccion not in productos:
        return "Producto no existe", monedas

    # Verificar si el dinero es suficiente
    producto = productos[seleccion]
    if total < producto[1]:
        return "Dinero insuficiente", monedas

    # Calcular cambio
    cambio = total - producto[1]
    cambio_monedas = []

    for m in sorted(monedas_soportadas, reverse=True):
        while cambio >= m:
            cambio -= m
            cambio_monedas.append(m)

    return producto[0], cambio_monedas


# Ejemplo de uso
print(maquina_expendedora([200], 1))  # ('Coca-Cola', 100)
print(maquina_expendedora([50], 2))  # ('Papas', 0)
print(maquina_expendedora([10], 3))  # ('Dinero insuficiente', 10)
print(maquina_expendedora([80], 3))  # ('Moneda no soportada', 80)
print(maquina_expendedora([100], 3))  # ('Chocolate', 25)
