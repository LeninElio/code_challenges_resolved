import csv


def game_date(name):
    with open('data_legends.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            return row[name]


game_date('The Legend of Zelda: Skyward Sword')

