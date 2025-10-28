import csv

with open('Bestseller - Sheet1.csv', encoding='utf-8') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)