import csv

with open('data_legends.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row[0], row[1])

