"""
Reto #5
ASPECT RATIO DE UNA IMAGEN
Fecha publicación enunciado: 01/02/22
Fecha publicación resolución: 07/02/22
Dificultad: DIFÍCIL
 *
Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
- Nota: Esta prueba no se puede resolver con el playground online de Kotlin. Se necesita Android Studio.
- Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png
- Por ratio hacemos referencia por ejemplo a los "16:9" de una imagen de 1920*1080px.
 *
Información adicional:
- Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁 reto-semanal" para preguntas, dudas o prestar ayuda
  a la comunidad.
- Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
- Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
- Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
"""

from PIL import Image

# Abrimos la imagen
url = Image.open('../data/mouredev_github_profile.png')

# Enlistamos los formatos en un diccionario
formatos = {
    'f1': {'Relación': '4:3', 'Valor': 1.33, 'Descripción': 'Formato para monitores de computadora del siglo XX'},
    'f2': {'Relación': '2:1', 'Valor': 1.41, 'Descripción': 'Tamaños de papel internacionales (ISO 216)'},
    'f3': {'Relación': '3:2', 'Valor': 1.5, 'Descripción': 'película de cámara fija de 35 mm , pantallas de iPhone ('
                                                           'hasta iPhone 5)'},
    'f4': {'Relación': '16:10', 'Valor': 1.6, 'Descripción': 'Pantallas de computadora de pantalla ancha de uso común '
                                                             '(WXGA)'},
    'f5': {'Relación': 'Φ:1', 'Valor': 1.618, 'Descripción': 'Proporción áurea , cerca de 16:10'},
    'f6': {'Relación': '5:3', 'Valor': 1.66, 'Descripción': 'Super 16 mm , un calibre de película estándar en muchos '
                                                            'países europeos'},
    'f7': {'Relación': '16:9', 'Valor': 1.77, 'Descripción': 'TV de pantalla ancha y la mayoría de las computadoras '
                                                             'portátiles'},
    'f8': {'Relación': '2:1', 'Valor': 2, 'Descripción': 'Fichas de dominó'},
    'f9': {'Relación': '64:27', 'Valor': 2.370, 'Descripción': 'Pantalla ultra ancha, 21:9'},
    'f10': {'Relación': '32:9', 'Valor': 3.5, 'Descripción': 'Pantalla súper ultra ancha'},
    'f11': {'Relación': '19:10', 'Valor': 1.9, 'Descripción': 'Cines IMAX'},
}

# obtenemos el ancho y el alto
ancho, alto = url.size

# print(ancho, alto)
resultado = ancho / alto
# resultado = 1920/1080

# for i in formatos:
#     for j in formatos[i]:
#         print(formatos[i][j])
#     print('----------')

print(f'Ancho de la imagen {ancho}px')
print(f'Alto de la imagen {alto}px')

for i in formatos:
    # print(round(formatos[i]['Valor'], 1))
    if resultado == formatos[i]['Valor']:
        print(f'Resultado obtenido {round(resultado, 2)}, pertenece a la Relación {formatos[i]["Relación"]}: '
              f'{formatos[i]["Descripción"]}')
else:
    print(f'El resultado {round(resultado, 2)} no se adecua a ningún formato conocido')

