import csv
import pandas as pd

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

def dataWriterDataset(dataset):
    print("Export dataframe to csv (folder where script is run from) ..... \n")
    df = pd.DataFrame(dataset)
    df.to_csv('logfile.csv', index=False, header=False, sep=';')
    print("Done.\n")