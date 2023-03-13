# Nota (Lenin Elio - 13/03/2023 16:08), esta function busca un año bisiesto
def an_bisiesto(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Nota (Lenin Elio - 13/03/2023 15:59), búsqueda de los 30 primeros años bisiesto
a_inicio = int(input('Ingrese un año de inicio: '))
lista = [year for year in range(a_inicio, a_inicio + 130) if an_bisiesto(year)][:30]
print(lista)
print(len(lista))

# Nota (Lenin Elio - 13/03/2023 16:20), otra manera podría ser, este es menos legible:
y = int(input('Ingrese un año de inicio: '))
lista = [year for year in range(y, y + 130) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)][:30]
print(lista)
print(len(lista))

# Nota (Lenin Elio - 13/03/2023 16:23), otra manera, este es mas legible
y = int(input('Ingrese un año de inicio: '))
lista = [year for year in range(y, y + 130) if an_bisiesto(year)][:30]
print(lista)
print(len(lista))
