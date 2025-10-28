import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]


with open('packing_list.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(data)

with open('packing_list.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    print(next(csv_reader))