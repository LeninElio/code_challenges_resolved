datos = ['5', '+', '2', '-', '1', '*', '8', '-', '15', '+', '4', '/', '2']
# datos = ['5', '-', '4']
# conversion = []
# operadores = []
# for i in datos:
#     try:
#         conversion.append(float(i))
#     except ValueError:
#         conversion.append(i)
#         operadores.append(i)
#
# print(conversion)
# print(operadores)
#
# resultado = 0
# operador = '+'
# for i in range(len(conversion)):
#     if i == 0:
#         resultado = conversion[i]
#         continue
#     if conversion[i] in operadores:
#         operador = conversion[i]
#         continue
#     else:
#         if operador == '+':
#             resultado += conversion[i]
#         elif operador == '-':
#             resultado -= conversion[i]
#         elif operador == '*':
#             resultado *= conversion[i]
#         elif operador == '/':
#             resultado /= conversion[i]
#
# print(f'este es el resultado final {resultado}')
# print(f'este es el operador final {operador}')


# words = ["rain", "sun", "moon", "weather", "exit"]
#
# for word in words:
#     # checking for the breaking condition
#     if word == "exit":
#         # if the condition is true, then break the loop
#         break
#     if word == "moon":
#         # this statement will be executed
#         # print("moon is skipped")
#         continue
#         # this statement won't be executed
#         # print("This won't be printed")
#         # Otherwise, print the word
#     print(word)
