# En un polígono regular, el perímetro se puede determinar por el producto del número de lados por la longitud de uno
# de los lados, es decir, Perímetro=N·L. O sea:

import math

n = int(input('Numero de lados del polígono: '))
l = int(input('Cuanto mide el lado del polígono?: '))

teta = 360 / (2 * n)
print(f'El ángulo mide {teta}°')

# Convertimos los grados de teta a radianes
radianes = (teta * math.pi) / 180

# La apotema ap. de un polígono regular es la distancia de cualquier de sus lados al centro (C) del polígono.
ap = l / (2 * math.tan(radianes))
print(f'El apotema = {round(ap, 2)}')

# área del polígono
area = (n * l * ap) / 2
print(f'El area del polígono = {round(area, 2)}')
