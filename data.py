import csv

def dataReaderNames():
    data = list(csv.reader(open('Testdaten.sortiert.csv'), delimiter=';'))
    names = []
    for line in data:
        if line[0] != "Name":
            names.append(line[0])
        else:
            print("Line filtered.")
    names_s = list(set(names))
    return names_s

#names = dataReaderNames()

