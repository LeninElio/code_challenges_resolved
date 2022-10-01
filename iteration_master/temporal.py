lista_1 = [2, 2]
lista_2 = [3]

lista2 = [i for i in lista_2 if i not in lista_1]

lista3 = lista_1 + lista2

multi = 1
for i in lista3:
    multi *= i

print(lista2)
print(lista3)
print(multi)
