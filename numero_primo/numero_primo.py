# Los números primos son aquellos que solo, muy importante, solo son divisibles (al dividirse entre otro da un
# número entero) entre ellos mismos y el 1.

# num = int(input('Ingrese el limite para calcular los números primos: '))
# i = 1
#
# while i <= num:
#     if i / 1 == i and i / i == 1:
#         print(f'np{i}')
#     else:
#         print(i)
#     i += 1

num = 2

if num == 2 or num == 3 or num == 5 or num == 7:
    print('primo')
elif num % 2 == 0:
    print(num)
elif num % 3 == 0:
    print(num)
elif num % 5 == 0:
    print(num)
elif num % 7 == 0:
    print(num)
else:
    print('primo')
