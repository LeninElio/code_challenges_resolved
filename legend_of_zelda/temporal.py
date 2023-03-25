import csv


def retorna_fecha(reader, game_i, game_ii):
    num = []
    nombres = []
    date = []
    for i in reader:
        num.append(i[0])
        nombres.append(i[1])
        date.append(i[2])

    game_i_index = nombres.index(game_i) if game_i in nombres else ''
    game_ii_index = nombres.index(game_ii) if game_ii in nombres else ''

    if game_i_index != '' or game_ii_index != '':
        return date[game_i_index], date[game_ii_index]
    else:
        return 'Juegos no encontrados'


def game_date(game_i, game_ii):
    with open('data_legends.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        fechas = retorna_fecha(reader, game_i, game_ii)
        if fechas != '':
            return fechas[0], fechas[1]
        else:
            return 'Revise los nombres de los juegos'


print(game_date('The Legend of Zelda: Skyward Sword', 'The Legend of Zelda: Oracle of Ages'))
