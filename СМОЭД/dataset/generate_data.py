import csv
from random import shuffle

SOURCE = 'source.csv'
OUTPUT = 'dataset.csv'
COUNT = 114

data = []

with open(SOURCE, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            data.append([int(row[0]), float(row[1])])
        except:
            pass

shuffle(data)

with open(OUTPUT, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["nu","E"])
    writer.writerows(data[:COUNT])

