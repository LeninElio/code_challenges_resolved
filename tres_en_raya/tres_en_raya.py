"""

/*
 * Reto #18
 * TRES EN RAYA
 * Fecha publicación enunciado: 02/05/22
 * Fecha publicación resolución: 09/05/22
 * Dificultad: DIFÍCIL
 *
 * Enunciado: Crea una función que analice una matriz 3x3 compuesta por "X" y "O" y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta. O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta. Se podría representar con un vacío "", por ejemplo.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */

"""


def analizar_tres_en_raya(tablero):
    # Comprobar si hay un ganador en las filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2]:
            if tablero[i][0] == "X":
                return "Ganador X"
            elif tablero[i][0] == "O":
                return "Ganador O"

    # Comprobar si hay un ganador en las columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i]:
            if tablero[0][i] == "X":
                return "Ganador X"
            elif tablero[0][i] == "O":
                return "Ganador O"

    # Comprobar si hay un ganador en las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        if tablero[0][0] == "X":
            return "Ganador X"
        elif tablero[0][0] == "O":
            return "Ganador O"

    if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        if tablero[0][2] == "X":
            return "Ganador X"
        elif tablero[0][2] == "O":
            return "Ganador O"

    # Si no hay ganadores, comprobar si hay un empate
    empate = True
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "":
                empate = False

    if empate:
        return "Empate"

    # Si no hay ganadores ni empate, la proporción no es correcta
    return "Nulo"


datos = [
    ["X", "O", "X"],
    ["O", "O", "X"],
    ["0", "X", "X"]
]

resultado = analizar_tres_en_raya(datos)

print(resultado)
