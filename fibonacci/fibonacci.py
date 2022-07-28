# Sucesión de fibonacci

numero = int(input('Ingrese el limite para ejecutar la sucesión de fibonacci: '))
a = [0, 1]

print(f'a0 = {a[0]}')
print(f'a1 = {a[1]}')
for i in range(2, numero):
    an = a[-1] + a[-2]
    a.append(an)
    print(f'a{i} = {an}')
print(f'a = {a}')

