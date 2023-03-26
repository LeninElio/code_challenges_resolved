"""

/*
 * Reto #37
 * LOS LANZAMIENTOS DE "THE LEGEND OF ZELDA"
 * Fecha publicación enunciado: 14/09/22
 * Fecha publicación resolución: 19/09/22
 * Dificultad: MEDIA
 *
 * Enunciado: ¡Han anunciado un nuevo "The Legend of Zelda"! Se llamará "Tears of the Kingdom"
 * y se lanzará el 12 de mayo de 2023.
 * Pero, ¿recuerdas cuánto tiempo ha pasado entre los distintos "The Legend of Zelda" de la historia?
 * Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda que tú selecciones.
 * - Debes buscar cada uno de los títulos y su día de lanzamiento (si no encuentras el día exacto
 * puedes usar el mes, o incluso inventártelo)
 *
 * Información adicional:
 * - Usa el canal de nuestro Discord (https://mouredev.com/discord) "🔁reto-semanal"
 *   para preguntas, dudas o prestar ayuda a la comunidad.
 * - Tienes toda la información sobre los retos semanales en
 *   https://retosdeprogramacion.com/semanales2022.
 *
 */

"""
import pandas as pd
from datetime import datetime
import locale

# Nota (Lenin Elio - 25/03/2023 16:12)
# Establecemos la configuración regional a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Cargamos los datos del archivo CSV
data = pd.read_csv('data_legends.csv')

# Pedimos al usuario que seleccione los dos juegos
juego1 = input('Ingresa el nombre del primer juego: ')
juego2 = input('Ingresa el nombre del segundo juego: ')

# Nota (Lenin Elio - 25/03/2023 16:17)
# Obtenemos las fechas de lanzamiento de los juegos seleccionados
try:
    fecha1 = data.loc[data['nombre_juego'] == juego1, 'fecha_lanzamiento'].values[0]
    fecha2 = data.loc[data['nombre_juego'] == juego2, 'fecha_lanzamiento'].values[0]
except IndexError:
    fecha1, fecha2 = 0, 0

if fecha1 != 0 or fecha2 != 0:
    # Convertimos las fechas a objetos datetime
    fecha1 = datetime.strptime(fecha1, '%d de %B de %Y')
    fecha2 = datetime.strptime(fecha2, '%d de %B de %Y')

    # Calculamos la diferencia en días entre las dos fechas
    diferencia = abs((fecha2 - fecha1).days)

    # Calculamos cuántos años y días hay en la diferencia
    years = diferencia // 365
    days = diferencia % 365

    print(f'Hay {years} años y {days} días entre {juego1} y {juego2}.')

else:
    print('Juego no encontrado.')
