import csv
print('app started')
try:
    with open('sample.csv','r') as f:
        rows = csv.reader(f)
        data = []
        for row in rows:
            print(row[0])
except FileNotFoundError:
    print('Double Check File existance')
