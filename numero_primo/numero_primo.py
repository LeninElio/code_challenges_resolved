# Los números primos son aquellos que solo, muy importante, solo son divisibles (al dividirse entre otro da un
# número entero) entre ellos mismos y el 1.

numero = int(input('Ingrese el limite para calcular los números primos: '))
# num = 2


for num in range(1, numero + 1):
    lista = []
    listas = []
    for n in range(2, num):
        div = num % n
        if div == 0:
            lista.append(n)
        else:
            listas.append(n)

    if not lista:
        # print(lista)
        print(f'{num} Es numero primo')
        # print('')
    else:
        # print(lista)
        print(num)
        # print('')
