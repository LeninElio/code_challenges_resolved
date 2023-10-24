# Sucesión de fibonacci

# numero = int(input('Ingrese el limite para ejecutar la sucesión de fibonacci: '))
# a = [0, 1]
#
# print(f'a0 = {a[0]}')
# print(f'a1 = {a[1]}')
# for i in range(2, numero):
#     an = a[-1] + a[-2]
#     a.append(an)
#     print(f'a{i} = {an}')
# print(f'a = {a}')
#


def fibo(n):
    a = [1, 2]
    for i in range(3, n):
        an = a[-1] + a[-2]
        a.append(an)

    print(sum([val for val in a if val % 2 == 0 and val <= n]))


def fibonn(n):
    a, b = 1, 2
    suma = 0
    while a <= n:

        if a % 2 == 0:
            print(a)
            suma += a
        a, b = b, a + b

    print('---->', suma)


numeros = [10]
for numero in numeros:
    fibonn(numero)
