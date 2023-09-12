# num = ['s', 'a', 'l', 't', 'e']

# for i in num:
#     dato = [nume for nume in num if nume != i]
#     for j in dato:
#         dato2 = [nume for nume in dato if nume != j]
#         for k in dato2:
#             dato3 = [nume for nume in dato2 if nume != k]
#             for l in dato3:
#                 dato4 = [nume for nume in dato3 if nume != l]
#                 print([i, j, k, l, dato4[0]])


def permutaciones(lista, tamano):
    """
    Genera todas las permutaciones posibles de una lista de elementos.
    """
    if tamano == 1:
        return [[i] for i in lista]
    respuesta = []
    for i in lista:
        dato = [elemento for elemento in lista if elemento != i]
        for j in permutaciones(dato, tamano-1):
            respuesta.append([i] + j)
    return respuesta


if __name__ == "__main__":
    PALABRA = "sal"
    palabra = list(PALABRA)
    res = permutaciones(palabra, len(palabra))
    if len(res) == 0:
        print("La palabra tiene letras repetidas.")
    else:
        print(f"Se encontraron {len(res)} permutaciones:")
        for r in res:
            print(''.join(r))
