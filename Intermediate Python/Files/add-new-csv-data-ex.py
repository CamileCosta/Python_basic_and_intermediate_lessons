import csv

data_to_write = [
    ["Ed & Lorraine Warren - Dark Place", 'Ed Warren & Lorraine Warren', 'English', '1992', '10000', 'Horror' ]
]

with open('Bestseller - Sheet1.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(data_to_write)