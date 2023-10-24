# for i in range(10):
#     if str(i) == str(i)[::-1]:
#         print(i)
#         # break


def find_multi_bc(num):
    for i in range(100, 1000):
        if num % i == 0:
            j = num // i
            if 100 <= j < 1000:
                return True
    return False


def find_multi(num):
    valores = []
    for it in range(100, 1000):
        if num % it == 0:
            valores.append(it)
    # print(valores)
    # for i in range(len(valores)):
    #     if i + 1 < len(valores) and valores[i] * valores[i+1] == num:
    #         print(num, '--->', [valores[i], valores[i+1]], '--->', valores[i] * valores[i+1], '--->', valores)
    #         return num
    for i in range(len(valores)):
        for j in range(i + 1, len(valores)):
            if valores[i] * valores[j] == num:
                return num


pal = 99999
pal = pal - 1
while pal > 0:
    if str(pal) == str(pal)[::-1]:
        if find_multi_bc(pal):
            print(pal, '---')
            break
    pal -= 1


# find_multi(100000)
# valores = [1, 2, 3, 4, 5, 6, 10, 15, 30]
# for i in range(len(valores)):
#     for j in range(i + 1, len(valores)):
#         if valores[i] * valores[j] == num:
#             print(valores[i], valores[j], valores[i] * valores[j])
#
